from subprocess import getoutput as run

from pyrogram import filters, Client 
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from info import DEV_USERS
from info import OWNER_ID

@Client.on_message(filters.command('devlist'))
def devlist(_, m):
      if m.from_user.id in DEV_USERS:
         m.reply(str(DEV_USERS))
      else:
          m.reply("only Devs can access this command!")
  
        
@Client.on_message(filters.user(DEV_USERS) & filters.command("sh", prefixes=['/', '.', '?', '-']))
def sh(_, m):
    if m.from_user.id in DEV_USERS:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        m.reply(
            f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")
    else:
        m.reply("only Devs can access this command!")

def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@Client.on_message(
    filters.command("logs", prefixes=[".", "/", ";", "," "*"]) & filters.user(dev_user)
)
def sendlogs(_, m: Message):
    logs = run("tail logs.txt")
    x = paste(logs)
    keyb = [
        [
            InlineKeyboardButton("Link", url=x),
            InlineKeyboardButton("File", callback_data="sendfile"),
        ],
    ]
    m.reply(x, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(keyb))

