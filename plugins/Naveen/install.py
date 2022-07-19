import os

from pyrogram import Client, filters
from plugins.helper_functions.startup_helpers import load_plugin
from plugins.helper_functions.basic_helpers import edit_or_reply


@Client.on_message(filters.command('install'))
async def installer(client, message):
    pablo = await message.reply_text("Processing...")
    if not message.reply_to_message:
        await pablo.edit("NEEDS_REPLY")
        return
    if not message.reply_to_message.document:
        await pablo.edit("IS_NOT_DOC")
        return
    file_name = message.reply_to_message.document.file_name
    ext = file_name.split(".")[1]
    if os.path.exists(os.path.join("./plugins/", file_name)):
        await pablo.edit("ALREADY_INSTALLED")
        return
    if ext.lower() != "py":
        await pablo.edit("ONLY_PY_FILES")
        return
    Escobar = await message.reply_to_message.download(file_name="./plugins/")
    base_name = os.path.basename(Escobar)
    file_n = base_name.split(".")[0]
    try:
        load_plugin(file_n)
    except Exception as e:
        await pablo.edit("ERROR_INSTALLING")
        os.remove(Escobar)
        return
     await pablo.edit("PLUGIN INSTALLED SUCCESSFULLY")
