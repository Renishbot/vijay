import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from info import PICS
from info import IMDB_TEMPLATE
from utils import extract_user, get_file_id, get_poster, last_online
import time
import random
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)



@Client.on_message(filters.command("help"))
async def help(client, message):
        buttons = [[
            InlineKeyboardButton('Approve', callback_data='approve'),
            InlineKeyboardButton('ᴀᴜᴅɪᴏ-ʙᴏᴏᴋ', callback_data='abook'),
            InlineKeyboardButton('ᴀᴜᴛᴏ ғɪʟᴛᴇʀ', callback_data='autofilter'),
            ],[
            InlineKeyboardButton('Bot Status', callback_data='restatus'),
            InlineKeyboardButton('boycott', callback_data='boycott'),
            InlineKeyboardButton('Carbon', callback_data='carbon'),
            ],[
            InlineKeyboardButton('collage', callback_data='collage'),
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴs', callback_data='coct'),
            InlineKeyboardButton('ᴄᴏᴠɪᴅ', callback_data='corona'),
            ],[
            InlineKeyboardButton('ᴇxᴛʀᴀ', callback_data='extra'),
            InlineKeyboardButton('ekart', callback_data='ekart'),
            InlineKeyboardButton('ғᴜɴ', callback_data='fun'),
            ],[
            InlineKeyboardButton('ғɪʟᴇ-sᴛᴏʀᴇ', callback_data='newdata'),
            InlineKeyboardButton('Github', callback_data='github'),
            InlineKeyboardButton('Greetings', callback_data='greetings'),
            ],[
            InlineKeyboardButton('ɢ-ᴛʀᴀɴs', callback_data='gtrans'),
            InlineKeyboardButton('IFSC', callback_data='ifsc'),
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data='image'),
            ],[
            InlineKeyboardButton('IP Address', callback_data='ip'),
            InlineKeyboardButton('ᴊsᴏɴ', callback_data='son'),
            InlineKeyboardButton('ᴋɪᴄᴋ', callback_data='zombies'),
            ],[
            InlineKeyboardButton('Locks', callback_data='lock'),
            InlineKeyboardButton('Lyrics', callback_data='lyrics'),
            InlineKeyboardButton('ᴍᴀʟʟᴜ ᴀᴜɴᴛʏ', callback_data='aunty'),
            ],[
            InlineKeyboardButton('ᴍᴀɴᴜeʟ ғɪʟᴛᴇʀ', callback_data='manuelfilter'),
            InlineKeyboardButton('ᴍᴀᴍᴍᴏᴋᴀ', callback_data='mammoka'),
            InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='restric'),
            ],[
            InlineKeyboardButton("Notes", callback_data='notes'),
            InlineKeyboardButton("OCR", callback_data='ocr'),
            InlineKeyboardButton('ᴘᴀsᴛᴇ', callback_data='pastes'),
            ],[
            InlineKeyboardButton('ᴘɪɴɢ', callback_data='pings'),
            InlineKeyboardButton('ᴘɪɴ', callback_data='pin'),
            InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purges'),
            ],[
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ', callback_data='report'),
            InlineKeyboardButton('Rules', callback_data='rules'),
            InlineKeyboardButton('sʜᴀʀᴇ-ᴛᴇxᴛ', callback_data='sharetext'),
            ],[
            InlineKeyboardButton('ᴘᴀssᴡᴏʀᴅ-ɢᴇɴ', callback_data='genpassword'),
            ],[
            InlineKeyboardButton('Shazam', callback_data='shazam'),
            InlineKeyboardButton('sᴛɪᴄᴋᴇʀ-ɪᴅ', callback_data='sticker'),
            InlineKeyboardButton('ՏTYᒪIՏᕼ ᖴOᑎTՏ', callback_data='fonts'),
            ],[
            InlineKeyboardButton('sᴏɴɢ', callback_data='songs'),
            InlineKeyboardButton('sᴏᴜʀᴄᴇ', callback_data='source'),
            InlineKeyboardButton('Text To Img', callback_data='img'),
            ],[
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='tele'),
            InlineKeyboardButton('ᴛᴏʀʀᴇɴᴛ', callback_data='torrent'),
            InlineKeyboardButton('ᴛᴛs', callback_data='ttss'),
            ],[
            InlineKeyboardButton('ᴜʀʟ-sʜᴏʀᴛ', callback_data='urlshort'),
            InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data='video'),
            InlineKeyboardButton('Warns', callback_data='warn'),
            ],[
            InlineKeyboardButton('ᴡʜᴏɪs', callback_data='whois'),
            InlineKeyboardButton('Wikipedia', callback_data='wikipedia'),
            InlineKeyboardButton('ʏᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb'),
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton('ᴄʟᴏsᴇ x', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_video(
            video="https://telegra.ph/file/dda9d42c0b0c2d9846049.mp4",
            caption=script.HELP_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )

@Client.on_message(filters.command("about"))
async def aboutme(client, message):
        buttons= [[
            InlineKeyboardButton('𝙂𝙞𝙩𝙝𝙪𝙗', url='https://github.com/Naveen-TG'),
            InlineKeyboardButton('𝙐𝙥𝙙𝙖𝙩𝙚𝙨', url='https://t.me/VijayTG_Updates'),
            InlineKeyboardButton('𝙎𝙩𝙖𝙩𝙨', callback_data='stats')
            ],[
            InlineKeyboardButton('𝘽𝙖𝙘𝙠', callback_data='start'),
            InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_video(
            video="https://telegra.ph/file/09f6001759b82ac9150dd.mp4",
            caption=script.ABOUTME_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )

@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('Searching ImDB')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("No results Found")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('Here is what i found on IMDb', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('Give me a movie / series Name')

@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, movie = query.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')} - {imdb.get('year')}",
                    url=imdb['url'],
                )
            ],
            [
                InlineKeyboardButton(
                    text=f"𝙈𝙤𝙫𝙞𝙚 𝙂𝙧𝙤𝙪𝙥",
                    url="https://t.me/TamilMV_Collections"
                )
            ],
        ]
    message = quer_y.message.reply_to_message or quer_y.message
    if imdb:
        caption = IMDB_TEMPLATE.format(
            query = imdb['title'],
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url']
        )
    else:
        caption = "No Results"
    if imdb.get('poster'):
        try:
            await query.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await query.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        except Exception as e:
            logger.exception(e)
            await query.message.reply(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
        await query.message.delete()
    else:
        await query.message.edit(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
    await query.answer()
        

        
