from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from info import ADMINS, SUDO_USERS, DEV_USERS
from os import execvp,sys,execl
from sys import executable


@Client.on_message(filters.command("restart") & ~filters.edited)
async def restart(_,message):
    try:
        if message.from_user.id not in DEV_USERS:
           await message.delete()
           await message.reply("Only bot admins can do this action⚠️") 
           return
        await message.delete()
        await message.reply_text("⚰️")
        execl(executable, executable, "tigershroff.py")
    except Exception as e:
        pass
        await message.reply((e))
