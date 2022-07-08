import os
from plugins.helper_functions.startup_helpers import load_plugin
from plugins.helper_functions.basic_helpers import edit_or_reply


@friday_on_cmd(
    ["install"],
    cmd_help={
        "help": "Install Custom Plugins In Userbot",
        "example": "{ch}install (replying to plugin (.py))",
    },
)
async def installer(client, message):
    engine = message.Engine
    pablo = await edit_or_reply(message, engine.get_string("PROCESSING"))
    if not message.reply_to_message:
        await pablo.edit(engine.get_string("NEEDS_REPLY").format("A Plugin"))
        return
    if not message.reply_to_message.document:
        await pablo.edit(engine.get_string("IS_NOT_DOC"))
        return
    file_name = message.reply_to_message.document.file_name
    ext = file_name.split(".")[1]
    if os.path.exists(os.path.join("./plugins/", file_name)):
        await pablo.edit(engine.get_string("ALREADY_INSTALLED"))
        return
    if ext.lower() != "py":
        await pablo.edit(engine.get_string("ONLY_PY_FILES"))
        return
    Escobar = await message.reply_to_message.download(file_name="./plugins/")
    base_name = os.path.basename(Escobar)
    file_n = base_name.split(".")[0]
    try:
        load_plugin(file_n)
    except Exception as e:
        await pablo.edit(engine.get_string("ERROR_INSTALLING").format(e))
        os.remove(Escobar)
        return
    await pablo.edit(engine.get_string("PLUGIN_INSTALLED").format(file_name))

def friday_on_cmd(
    cmd: list,
    group: int = 0,
    pm_only: bool = False,
    group_only: bool = False,
    chnnl_only: bool = False,
    only_if_admin: bool = False,
    ignore_errors: bool = False,
    propagate_to_next_handler: bool = True,
    disable_sudo: bool = False,
    file_name: str = None,
    is_official: bool = True,
    cmd_help: dict = {"help": "No One One Gonna Help You", "example": "{ch}what"},
):
    """- Main Decorator To Register Commands. -"""
    if disable_sudo:
        filterm = (
        filters.me
        & filters.command(cmd, Config.COMMAND_HANDLER)
        & ~filters.via_bot
        & ~filters.forwarded
    )
    else:
        filterm = (
            (filters.me | _sudo)
            & filters.command(cmd, Config.COMMAND_HANDLER)
            & ~filters.via_bot
            & ~filters.forwarded)
    cmd = list(cmd)
    add_help_menu(
        cmd=cmd[0],
        stack=inspect.stack(),
        is_official=is_official,
        cmd_help=cmd_help["help"],
        example=cmd_help["example"],
    )
