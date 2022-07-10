import os
import time
import requests
from pyrogram import Client, filters
from info import Config
from plugins import run_cmd
from plugins.helper_functions.basic_helpers import (
    edit_or_reply,
    progress,
    edit_or_send_as_file,
    get_text,
)

vak = Config.V_T_KEY

@Client.on_message(filters.command("scan"))
async def scan_my_file(client, message):
    ms_ = await message.reply_text("Please Wait! Scanning This File")
    if not message.reply_to_message:
      return await ms_.edit("`Please Reply To File To Scan For Viruses`")
    if not message.reply_to_message.document:
      return await ms_.edit("`Please Reply To File To Scan For Viruses`")
    if not vak:
      return await ms_.edit("`You Need To Set VIRUSTOTAL_API_KEY For Functing Of This Plugin.`")
    if int(message.reply_to_message.document.file_size) > 25000000:
      return await ms_.edit("`File Too Large , Limit is 25 Mb`")
    c_time = time.time()
    downloaded_file_name = await message.reply_to_message.download(progress=progress, progress_args=(ms_, c_time, f"`Downloading This File!`"))
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    params = {"apikey": vak}
    files = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    response = requests.post(url, files=files, params=params)
    try:
       r_json = response.json()
       scanned_url = r_json["permalink"]
    except:
      return await ms_.edit(f"`[{response.status_code}] - Unable To Scan File.`")
    await ms_.edit(f"<b><u>Scanned {message.reply_to_message.document.file_name}</b></u>. <b>You Can Visit :</b> {scanned_url} <b>In 5-10 Min To See File Report</b>")
