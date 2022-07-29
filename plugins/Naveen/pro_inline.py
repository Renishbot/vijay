from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup 
try:
    from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
except Exception as e:
    pass
    print(e)
@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[

            InlineQueryResultArticle(
                title="Naveen",
                description="Click Here",
                thumb_url="https://telegra.ph/file/a91ddf16775ec8ef0bd9e.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Owner of the Bot"""
                ),
                reply_markup=InlinekeyboardMarkup([[
                    Inlinekeyboardbutton("Onwer", url="t.me/Naveen_TG")
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
            )
        ],
        cache_time=0
    )
