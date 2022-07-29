from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
                title="Naveen",
                description="Click Here",
                thumb_url="https://telegra.ph/file/a91ddf16775ec8ef0bd9e.jpg",
                input_message_contect=InputTextMessageContent(
                    message_text="""Owner of the Bot"""
                )
            )
        ],
        cache_tine=0
    )
