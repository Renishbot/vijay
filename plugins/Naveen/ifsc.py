import requests
from pyrogram  import Client, filters
from plugins.helper_functions.basic_helpers import edit_or_reply, get_text, edit_or_send_as_file, get_user


@Client.on_message(filters.command('ifsc'))
async def geT_if(client, message):
    m_ = await edit_or_reply(message, "`Please Wait!`")
    input_str = message.text.split(None, 1)[1]
    if not input_str:
        return await edit("Give Me IFSC Code As Input.")
    IFSC_Code = input_str
    URL = "https://ifsc.razorpay.com/"
    data = requests.get(URL + IFSC_Code)
    if "Not Found" in data.text:
        return await m_.edit("`404: IFSC CODE NOT FOUND.`") 
    try:
        data = data.json()
    except:
        return await m_.edit("`Invalid IFSC Code!`") 
    a = data["ADDRESS"]
    b = data["CENTRE"]
    c = data["BRANCH"]
    d = data["CITY"]
    e = data["STATE"]
    f = data["BANK"]
    g = data["BANKCODE"]
    h = data["IFSC"]
    await m_.edit(
        f"<b><u>INFORMATION GATHERED SUCCESSFULLY</b></u>\n\n<b>Bank Name :</b> <code>{f}</code>\n<b>Bank Address :</b> <code>{a}</code>\n<b>Centre :</b> <code>{b}</code>\n<b>Branch :</b> <code>{c}</code>\n<b>City :</b> <code>{d}</code>\n<b>State :</b> <code>{e}</code>\n<b>Bank Code :</b> <code>{g}</code>\n<b>IFSC :</b> <code>{h}</code>",
        parse_mode="html",
    )
