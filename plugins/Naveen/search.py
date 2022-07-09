import re
import urllib
import urllib.parse

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.helper_functions.basic_helpers import get_text
from plugins.CrazyBoss.friday import edit_or_reply
@Client.on_message(filters.command(["duckduckgo","ddg"]))
async def duckduckgo(client, message):
    pablo = await message.reply_text("Processing..."))
    query = get_text(message)
    if not query:
        await pablo.edit("No Input Found")
        return
    sample_url = "https://duckduckgo.com/?q={}".format(query.replace(" ", "+"))
    link = sample_url.rstrip()
    await pablo.edit("File Not Found")
    return


@Client.on_message(filters.command(["gs","grs","Google"]))
async def grs(client, message):
    pablo = await message.reply_text("Processing...")
    query = get_text(message)
    if not query:
        await pablo.edit(engine.get_string("INPUT_REQ").format("query"))
        return
    query = urllib.parse.quote_plus(query)
    number_result = 8
    ua = UserAgent()
    google_url = (
        "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    )
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result_div = soup.find_all("div", attrs={"class": "ZINbbc"})
    links = []
    titles = []
    descriptions = []
    for r in result_div:
        try:
            link = r.find("a", href=True)
            title = r.find("div", attrs={"class": "vvjwJb"}).get_text()
            description = r.find("div", attrs={"class": "s3v9rd"}).get_text()
            if link != "" and title != "" and description != "":
                links.append(link["href"])
                titles.append(title)
                descriptions.append(description)

        except:
            continue
    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search("\/url\?q\=(.*)\&sa", l)
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))
    for x in to_remove:
        del titles[x]
        del descriptions[x]
    msg = "".join(
        f"[{tt}]({liek})\n`{d}`\n\n"
        for tt, liek, d in zip(titles, clean_links, descriptions)
    )


    await pablo.edit("**Search Query:**\n`" + query + "`\n\n**Results:**\n" + msg)
