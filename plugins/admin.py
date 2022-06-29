import asyncio
import re

from time import time
from pyrogram.errors import FloodWait
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    ChatPermissions,
    Message,
)

from info import BOT_ID, SUDO_USERS
from plugins.Naveen.Masterolic.errors import capture_err
from plugins.Naveen.Masterolic.keyboard import ikb
from plugins.Naveen.Masterolic.Telegram.dbfunctions import (
    add_warn,
    get_warn,
    int_to_alpha,
    remove_warns,
    save_filter,
)
from plugins.Naveen.Masterolic.Telegram.functions import (
    extract_user,
    extract_user_and_reason,
    time_converter,
)

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
    except Exception:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms

