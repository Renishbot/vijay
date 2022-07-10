import requests
from pyrogram import Client, filters
from plugins.helper_functions.basic_helpers import edit_or_reply, get_text


@Client.on_message(filters.command('ekart'))
async def ekart(client, message):
    pablo = await message.reply_text("Processing...")
    input_str = message.text.split(None, 1)[1]
    if not input_str:
        await pablo.edit("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return
    urlo = (
        "https://track.aftership.com/trackings?courier=ekart&tracking-numbers="
        + str(input_str)
    )

    url = "https://ekart-api-chi.vercel.app/check?id=" + str(input_str)
    r = requests.get(url)
    h = r.json()
    merchant = h.get("merchant_name")
    order_status = h.get("order_status")
    kk = h.get("updates")
    oqwz = kk[0]
    aq = oqwz.get("Date")
    ar = oqwz.get("Time")
    place = oqwz.get("Place")
    status = oqwz.get("Status")

    caption = f""" <b>Ekart Tracking </b>
Merchant Name:- {merchant}
Order Status:- {order_status}
Tracking Id:- {input_str}
Latest Update
Date:- {aq}
Time:- {ar}
Place:- {place}
Status:- {status}
Detailed link:- {urlo}
<u><b>Ekart Search Completed By Friday.
Get Your Own Friday From @FRIDAYCHAT.</b></u>
"""
    await pablo.edit(caption, parse_mode="HTML")
