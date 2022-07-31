from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[

            InlineQueryResultArticle(
                title="Main Menu",
                description="Main Menu of the BoT",
                thumb_url="https://telegra.ph/file/75c9be07bb6e2a9309041.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Main Menu of the Bot, Here You Can Get A-Z Regarding the BoT"""
                ),
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('🛠️ 𝙃𝙚𝙡𝙥', callback_data='inline_help'),
                    InlineKeyboardButton('⭕️ 𝘼𝙗𝙤𝙪𝙩', callback_data='inline_about')
                    ]]
                )
            ),

            InlineQueryResultArticle(
                title="About the Bot",
                description="Show the Details of the Bot and Show the Purpose of Vijay BoT",
                thumb_url="https://telegra.ph/file/6b541273159cc36fa11d4.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Here is the All Details of the BoT"""
                )
            )
        ],
        cache_time=0
    )
