import re
from asyncio import sleep
from html import escape
from os import remove
from traceback import format_exc
from typing import List, Dict, Tuple, Optional


from pyrogram import filters
from pyrogram.errors import (
    ChatAdminInviteRequired,
    ChatAdminRequired,
    FloodWait,
    RightForbidden,
    RPCError,
    UserAdminInvalid,
)
from pyrogram.types import Message

from info import DEV_USERS, LOGGER, OWNER_ID, SUPPORT_GROUP, SUPPORT_STAFF
from pyrogram import Client as Alita
from plugins.Group.database.approve_db import Approve
from plugins.Group.database.reporting_db import Reporting
from plugins.Group.tr_engine import tlang
from plugins.Group.utils.caching import ADMIN_CACHE, TEMP_ADMIN_CACHE_BLOCK, admin_cache_reload
from plugins.Group.utils.custom_filters import (
    admin_filter,
    command,
    owner_filter,
    promote_filter,
)
from plugins.Group.utils.extract_user import extract_user
from plugins.Group.utils.parser import mention_html
from info import Config
from Wbb.permissions import adminsOnly


@Alita.on_message(command("adminlist"))
async def adminlist_show(_, m: Message):
    if m.chat.type != "supergroup":
        return await m.reply_text(
            "This command is made to be used in groups only!",
        )
    try:
        try:
            admin_list = ADMIN_CACHE[m.chat.id]
            note = "<i>Note:</i> These are cached values!"
        except KeyError:
            admin_list = await admin_cache_reload(m, "adminlist")
            note = "<i>Note:</i> These are up-to-date values!"

        adminstr = ("Admins in <b>{}</b>:").format(
            m.chat.title,
        ) + "\n\n"

        bot_admins = [i for i in admin_list if (i[1].lower()).endswith("bot")]
        user_admins = [i for i in admin_list if not (i[1].lower()).endswith("bot")]

        # format is like: (user_id, username/name,anonyamous or not)
        mention_users = [
            (
                admin[1]
                if admin[1].startswith("@")
                else (await mention_html(admin[1], admin[0]))
            )
            for admin in user_admins
            if not admin[2]  # if non-anonyamous admin
        ]
        mention_users.sort(key=lambda x: x[1])

        mention_bots = [
            (
                admin[1]
                if admin[1].startswith("@")
                else (await mention_html(admin[1], admin[0]))
            )
            for admin in bot_admins
        ]
        mention_bots.sort(key=lambda x: x[1])

        adminstr += "<b>User Admins:</b>\n"
        adminstr += "\n".join(f"- {i}" for i in mention_users)
        adminstr += "\n\n<b>Bots:</b>\n"
        adminstr += "\n".join(f"- {i}" for i in mention_bots)

        await m.reply_text(adminstr + "\n\n" + note)
        LOGGER.info(f"Adminlist cmd use in {m.chat.id} by {m.from_user.id}")

    except Exception as ef:
        if str(ef) == str(m.chat.id):
            await m.reply_text("Use /admincache to reload admins!")
        else:
            ef = f"{str(ef)}{admin_list}\n"
            await m.reply_text("Something went wrong!")
        LOGGER.error(ef)
        LOGGER.error(format_exc())

    return


@Alita.on_message(command("zombies") & owner_filter)
async def zombie_clean(c: Alita, m: Message):

    zombie = 0

    wait = await m.reply_text("Searching ... and banning ...")
    async for member in c.iter_chat_members(m.chat.id):
        if member.user.is_deleted:
            zombie += 1
            try:
                await c.kick_chat_member(m.chat.id, member.user.id)
            except UserAdminInvalid:
                zombie -= 1
            except FloodWait as e:
                await sleep(e.x)
    if zombie == 0:
        return await wait.edit_text("Group is clean!")
    return await wait.edit_text(
        f"<b>{zombie}</b> Zombies found and has been banned!",
    )


@Alita.on_message(command("admincache"))
async def reload_admins(_, m: Message):

    if m.chat.type != "supergroup":
        return await m.reply_text(
            "This command is made to be used in groups only!",
        )

    if (
        (m.chat.id in set(TEMP_ADMIN_CACHE_BLOCK.keys()))
        and (m.from_user.id) not in SUPPORT_STAFF
        and TEMP_ADMIN_CACHE_BLOCK[m.chat.id] == "manualblock"
    ):
        await m.reply_text("Can only reload admin cache once per 10 mins!")
        return

    try:
        await admin_cache_reload(m, "admincache")
        TEMP_ADMIN_CACHE_BLOCK[m.chat.id] = "manualblock"
        await m.reply_text("Successful reloaded the Admincache in this chat")
        LOGGER.info(f"Admincache cmd use in {m.chat.id} by {m.from_user.id}")
    except RPCError as ef:
        await m.reply_text("Something went wrong!")
        LOGGER.error(ef)
        LOGGER.error(format_exc())
    return


@Alita.on_message(filters.regex(r"^(?i)@admin(s)?") & filters.group)
async def tag_admins(_, m: Message):
    db = Reporting(m.chat.id)
    if not db.get_settings():
        return

    try:
        admin_list = ADMIN_CACHE[m.chat.id]
    except KeyError:
        admin_list = await admin_cache_reload(m, "adminlist")

    user_admins = [i for i in admin_list if not (i[1].lower()).endswith("bot")]
    mention_users = [(await mention_html("\u2063", admin[0])) for admin in user_admins]
    mention_users.sort(key=lambda x: x[1])
    mention_str = "".join(mention_users)
    await m.reply_text(
        (
            f"{(await mention_html(m.from_user.first_name, m.from_user.id))}"
            f" reported the message to admins!{mention_str}"
        ),
    )

@Alita.on_command("promote", about={
    'header': "use this to promote group members",
    'description': "Provides admin rights to the person in the supergroup.\n"
                   "you can also add custom title while promoting new admin.\n"
                   "[NOTE: Requires proper admin rights in the chat!!!]",
    'examples': [
        "{tr}promote [username | userid] or [reply to user] :custom title (optional)",
        "{tr}promote @someusername/userid/replytouser Staff (custom title)"]},
    allow_channels=False, check_promote_perm=True)
async def promote_usr(message: Message):
    """ promote members in tg group """
    user_id, custom_rank = message.extract_user_and_text
    if not user_id:
        await message.err("no valid user_id or message specified")
        return
    if custom_rank:
        custom_rank = get_emoji_regexp().sub(u'', custom_rank)
        if len(custom_rank) > 15:
            custom_rank = custom_rank[:15]

    await message.edit("`Trying to Promote User.. Hang on!! ⏳`")
    chat_id = message.chat.id
    try:
        await message.client.promote_chat_member(chat_id, user_id,
                                                 ChatPrivileges(can_invite_users=True,
                                                                can_pin_messages=True))
        if custom_rank:
            await asyncio.sleep(2)
            await message.client.set_administrator_title(chat_id, user_id, custom_rank)
    except UsernameInvalid:
        await message.err("`invalid username, try again with valid info ⚠`")
    except PeerIdInvalid:
        await message.err("invalid username or userid, try again with valid info ⚠")
    except UserIdInvalid:
        await message.err("invalid userid, try again with valid info ⚠")
    except Exception as e_f:
        await message.err(f"something went wrong! 🤔\n\n`{e_f}`")
    else:
        await message.edit("`👑 Promoted Successfully..`", del_in=5)
        user = await message.client.get_users(user_id)
        await CHANNEL.log(
            "#PROMOTE\n\n"
            f"USER: [{user.first_name}](tg://user?id={user_id}) (`{user_id}`)\n"
            f"CUSTOM TITLE: `{custom_rank or None}`\n"
            f"CHAT: `{message.chat.title}` (`{chat_id}`)")


@Alita.on_message(command("demote") & promote_filter)
async def demote_usr(c: Alita, m: Message):

    global ADMIN_CACHE

    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text("I can't demote nothing!")
        return

    try:
        user_id, user_first_name, _ = await extract_user(c, m)
    except Exception:
        return

    if user_id == Config.BOT_ID:
        await m.reply_text("Get an admin to demote me!")
        return

    # If user not alreay admin
    try:
        admin_list = {i[0] for i in ADMIN_CACHE[m.chat.id]}
    except KeyError:
        admin_list = {
            i[0] for i in (await admin_cache_reload(m, "demote_cache_update"))
        }

    if user_id not in admin_list:
        await m.reply_text(
            "This user is not an admin, how am I supposed to re-demote them?",
        )
        return

    try:
        await m.chat.promote_member(
            user_id=user_id,
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_voice_chats=False,
        )
        LOGGER.info(f"{m.from_user.id} demoted {user_id} in {m.chat.id}")

        # ----- Remove admin from cache -----
        try:
            admin_list = ADMIN_CACHE[m.chat.id]
            user = next(user for user in admin_list if user[0] == user_id)
            admin_list.remove(user)
            ADMIN_CACHE[m.chat.id] = admin_list
        except (KeyError, StopIteration):
            await admin_cache_reload(m, "demote_key_stopiter_error")

        await m.reply_text(
            ("{} demoted {} in <b>{}</b>!").format(
                (
                    await mention_html(
                        m.from_user.first_name,
                        m.from_user.id,
                    )
                ),
                (await mention_html(user_first_name, user_id)),
                m.chat.title,
            ),
        )

    except ChatAdminRequired:
        await m.reply_text("I'm not Admin here!")
    except RightForbidden:
        await m.reply_text("I don't have a right!")
    except UserAdminInvalid:
        await m.reply_text("Cannot act on this user, maybe I wasn't the one who changed their permissions.")
    except RPCError as ef:
        await m.reply_text("Something went wrong!")
        LOGGER.error(ef)
        LOGGER.error(format_exc())

    return


@Alita.on_message(command("setgtitle") & admin_filter)
async def setgtitle(_, m: Message):
    user = await m.chat.get_member(m.from_user.id)

    if not user.can_change_info and user.status != "creator":
        await m.reply_text(
            "You don't have enough permission to use this command!",
        )
        return False

    if len(m.command) < 1:
        return await m.reply_text("Please read /help for using it!")

    gtit = m.text.split(None, 1)[1]
    try:
        await m.chat.set_title(gtit)
    except Exception as e:
        return await m.reply_text(f"Error: {e}")
    return await m.reply_text(
        f"Successfully Changed Group Title From {m.chat.title} To {gtit}",
    )


@Alita.on_message(command("setgdes") & admin_filter)
async def setgdes(_, m: Message):

    user = await m.chat.get_member(m.from_user.id)
    if not user.can_change_info and user.status != "creator":
        await m.reply_text(
            "You don't have enough permission to use this command!",
        )
        return False

    if len(m.command) < 1:
        return await m.reply_text("Please read /help for using it!")

    desp = m.text.split(None, 1)[1]
    try:
        await m.chat.set_description(desp)
    except Exception as e:
        return await m.reply_text(f"Error: {e}")
    return await m.reply_text(
        f"Successfully Changed Group description From {m.chat.description} To {desp}",
    )


@Alita.on_message(command("title") & admin_filter)
async def set_user_title(c: Alita, m: Message):

    user = await m.chat.get_member(m.from_user.id)
    if not user.can_promote_members and user.status != "creator":
        await m.reply_text(
            "You don't have enough permission to use this command!",
        )
        return False

    if len(m.text.split()) == 1 and not m.reply_to_message:
        return await m.reply_text("To whom??")

    if m.reply_to_message:
        if len(m.text.split()) >= 2:
            reason = m.text.split(None, 1)[1]
    elif len(m.text.split()) >= 3:
        reason = m.text.split(None, 2)[2]
    try:
        user_id, _, _ = await extract_user(c, m)
    except Exception:
        return

    if not user_id:
        return await m.reply_text("Cannot find user!")

    if user_id == Config.BOT_ID:
        return await m.reply_text("Huh, why ?")

    if not reason:
        return await m.reply_text("Read /help please!")

    from_user = await c.get_users(user_id)
    title = reason
    try:
        await c.set_administrator_title(m.chat.id, from_user.id, title)
    except Exception as e:
        return await m.reply_text(f"Error: {e}")
    return await m.reply_text(
        f"Successfully Changed {from_user.mention}'s Admin Title To {title}",
    )


@Alita.on_message(command("setgpic") & admin_filter)
async def setgpic(c: Alita, m: Message):
    user = await m.chat.get_member(m.from_user.id)
    if not user.can_change_info and user.status != "creator":
        await m.reply_text(
            "You don't have enough permission to use this command!",
        )
        return False
    if not m.reply_to_message:
        return await m.reply_text("Reply to a photo to set it as chat photo")
    if not m.reply_to_message.photo and not m.reply_to_message.document:
        return await m.reply_text("Reply to a photo to set it as chat photo")
    photo = await m.reply_to_message.download()
    try:
        await m.chat.set_photo(photo)
    except Exception as e:
        remove(photo)
        return await m.reply_text(f"Error: {e}")
    await m.reply_text("Successfully Changed Group Photo!")
    remove(photo)

@Alita.on_message(
    filters.command(["promote", "fullpromote"])
    & ~filters.edited
    & ~filters.private
)
@adminsOnly("can_promote_members")
async def promoteFunc(_, message: Message):
    user_id = await extract_user(message)
    umention = (await app.get_users(user_id)).mention
    if not user_id:
        return await message.reply_text("I can't find that user.")
    bot = await app.get_chat_member(message.chat.id, BOT_ID)
    if user_id == BOT_ID:
        return await message.reply_text("I can't promote myself.")
    if not bot.can_promote_members:
        return await message.reply_text("I don't have enough permissions")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=bot.can_restrict_members,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        return await message.reply_text(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id=user_id,
        can_change_info=False,
        can_invite_users=bot.can_invite_users,
        can_delete_messages=bot.can_delete_messages,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=bot.can_manage_chat,
        can_manage_voice_chats=bot.can_manage_voice_chats,
    )
    await message.reply_text(f"Promoted! {umention}")



__PLUGIN__ = "admin"

__alt_name__ = [
    "admins",
    "promote",
    "demote",
    "adminlist",
    "setgpic",
    "title",
    "setgtitle",
    "fullpromote",
    "invitelink",
    "setgdes",
    "zombies",
]
