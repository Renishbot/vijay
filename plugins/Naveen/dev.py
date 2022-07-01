import io
import sys
import time
StartTime = time.time()
import traceback
from subprocess import getoutput as run

from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from requests import post

from nksama import dev_user
from nksama.config import OWNER_ID
from nksama import bot as app
from nksama import bot


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@bot.on_message(filters.command('devlist'))
def devlist(_, m):
      if m.from_user.id in dev_user:
         m.reply(str(dev_user))
      else:
          m.reply("only Devs can access this command!")
  
        
@app.on_message(filters.user(OWNER_ID) & filters.command("sh", prefixes=['/', '.', '?', '-']))
def sh(_, m):
    if m.from_user.id in dev_user:
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
