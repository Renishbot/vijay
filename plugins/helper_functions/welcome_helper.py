from os import name
from pyrogram.methods import messages
from plugins import help_message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def call_back_in_filter(data):
    return filters.create(lambda flt, _, query: flt.data in query.data,
                          data=data)

def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        return bool(user_data.status == 'administrator'
                    or user_data.status == 'creator')
    except:
        # print('Not admin')
        return False
