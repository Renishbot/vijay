from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from info import LOG_GROUP, OWNER_ID, SUDO_USERS,
from os import execvp,sys



@Client.on_message(filters.command("restart") & filters.chat(OWNER_ID) & filters.private)
async def restart(_,message):
    await message.delete()
    execvp(sys.executable,[sys.executable,"-m","Client"])
