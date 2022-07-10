from info import Config
from pyrogram import Client, filters
from plugins.CrazyBoss.friday import run_cmd
from plugins.helper_functions.basic_helpers import edit_or_reply, get_text
from plugins.helper_functions.plugin_helpers import convert_to_image
import requests
import os
from base64 import b64decode



async def make_me_a_zombie(img_path):
    """Upload Image To The Secret Api"""
    path_ = {"image": (img_path, open(img_path, "rb"))}
    req = requests.post('https://deepgrave-image-processor-no7pxf7mmq-uc.a.run.app/transform', files=path_)
    return req.text

def base64_to_image(base_code):
    """Decode And Convert To image Format."""
    img_name = "zombie_by_FRIDAYUB.png"   
    with open(img_name,"wb") as f:
        f.write(b64decode(str(base_code))) 
        f.close()
    return img_name

@Client.on_message(filters.command('zombie'))
async def make_everyone_a_zombie(client, message):
    msg_ = await edit_or_reply(message, "`OwO, Making A Blood Sucking Zombie...`")
    if not message.reply_to_message:
        return await msg_.edit("`Please Reply To A Image With A Face.`")
    cool = await convert_to_image(message, client)
    if not cool:
        await msg_.edit("`Reply to a valid media first.`")
        return
    if not os.path.exists(cool):
        await msg_.edit("`Invalid Media!`")
        return
    zombie_base64 = await make_me_a_zombie(cool)
    if "face" in zombie_base64.lower():
        return await msg_.edit("`No Face Found In This Image.`")
    await msg_.edit("`Converting Image...`")
    img_ = base64_to_image(zombie_base64)
    await msg_.edit("`Uploading Now.`")
    if message.reply_to_message:
        await client.send_photo(
            message.chat.id,
            photo=img_,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_photo(message.chat.id, photo=img_)
    await msg_.delete()
    if os.path.exists(img_):
        os.remove(img_)
 
