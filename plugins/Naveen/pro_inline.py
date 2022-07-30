from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
                title="About BOT",
                description="Buttoned Details of Vijay will be Shown Here, Try it❤️",
                thumb_url="https://telegra.ph/file/75c9be07bb6e2a9309041.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Owner of the Bot"""
                    )
                )
          ],
        cache_time=0
    )
