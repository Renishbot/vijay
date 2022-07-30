from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[

            InlineQueryResultArticle(
                title="Bot Owner",
                description="Don't Judge the Book with its Cover",
                thumb_url="https://telegra.ph/file/a91ddf16775ec8ef0bd9e.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Owner of the Bot"""
                ),
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("Owner", url="t.me/Naveen_TG")
                    ]]
                )
            ),

            InlineQueryResultArticle(
                title="About the Bot",
                description="Show the Details of the Bot and Show the Purpose of Vijay BoT",
                thumb_url="https://telegra.ph/file/75c9be07bb6e2a9309041.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Here is the All Details of the BoT"""
                )
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("Owner", callback_data='help')
                    ]]
            )
        ],
        cache_time=0
    )
