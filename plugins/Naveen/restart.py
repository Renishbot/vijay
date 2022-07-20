from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from info import ADMINS, SUDO_USERS
from os import execvp,sys,execl
from sys import executable


@Client.on_message(filters.command("restart") & filters.chat(ADMINS))
async def restart(_,message):
    try:
        await message.delete()
        await message.reply_text("⚰️")
        execl(executable, executable, "tigershroff.py")
    except Exception as e:
        pass
        await message.reply((e))
