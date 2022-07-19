from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from info import OWNER_ID, SUDO_USERS
from os import execvp,sys
from sys import executable


@Client.on_message(filters.command("restart") & filters.chat(OWNER_ID))
async def restart(_,message):
    await message.delete()
    await message.reply_text("⚰️")
    execl(executable, executable, "start.sh")
