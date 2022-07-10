from pyrogram import Client, filters
from plugins.helper_functions.basic_helpers import edit_or_reply, get_text
import asyncio
import time

@Client.on_message(filters.command('mask'))
async def mask(client, message):
    pablo = await message.reply_text("Processing...")
    if not message.reply_to_message:
        await pablo.edit("Please Reply To A Image")
        return
    if (
        message.reply_to_message.sticker
        and message.reply_to_message.sticker.mime_type != "image/webp"
    ):
        return
    await message.reply_text("hazmat_suit_bot")
    time.sleep(1.5)
    try:
       messi = (await client.get_history("hazmat_suit_bot", 1))[0]
    except Exception as messi:
        print(messi)
    await message.reply_photo(messi.photo.file_id)
    await pablo.delete()
