import os

from pyrogram import Client, filters
from plugins.helper_functions.startup_helpers import load_plugin
from plugins.helper_functions.basic_helpers import edit_or_reply


@Client.on_message(filters.command('install'))
async def installer(client, message):
    pablo = await message.reply_text("Processing...")
    if not message.reply_to_message:
        await pablo.edit("Reply To a File To Install the Plugin")
        return
    if not message.reply_to_message.document:
        await pablo.edit("IS_NOT_DOC")
        return
    file_name = message.reply_to_message.document.file_name
    ext = file_name.split(".")[1]
    if os.path.exists(os.path.join("./plugins/", file_name)):
        await pablo.edit("This File is Already Installed")
        return
    if ext.lower() != "py":
        await pablo.edit("You can Install Only Python Files Which is in py Format")
        return
    Escobar = await message.reply_to_message.download(file_name="./plugins/")
    base_name = os.path.basename(Escobar)
    file_n = base_name.split(".")[0]
    try:
        load_plugin(file_n)
    except Exception as e:
        await pablo.edit("There is Some Errors in Installing this File Check Codes Clearly and Install Again")
        os.remove(Escobar)
        return
    await pablo.edit('This Plugin Successfully Installed To Vijay')
