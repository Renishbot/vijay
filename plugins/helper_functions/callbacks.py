import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)
import logging

elif query.data == "helpq":
        buttonss =[[InlineKeyboardButton(text="AutoFilter", callback_data="autofilter"),
             InlineKeyboardButton(text="Group Management",callback_data="grp")]]
        reply_markup = InlineKeyboardMarkup(buttonss) 
        await query.answer("𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗆𝗒 𝗆𝗈𝖽𝗎𝗅𝖾s")
        await query.edit_message_text(
            text=script.HELP_TXT,
            reply_markup=reply_markup,
            parse_mode='html')

elif query.data == "aboutq":
        buttons= [[
            InlineKeyboardButton('➕ 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🔍𝙎𝙚𝙖𝙧𝙘𝙝', switch_inline_query_current_chat=''),
            InlineKeyboardButton('🤖 𝙐𝙥𝙙𝙖𝙩𝙚𝙨', url='https://t.me/VijayTG_Updates')
            ],[
            InlineKeyboardButton('🛠️ 𝙃𝙚𝙡𝙥', callback_data='help'),
            InlineKeyboardButton('⭕️ 𝘼𝙗𝙤𝙪𝙩', callback_data='about')
        ]]                      
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
