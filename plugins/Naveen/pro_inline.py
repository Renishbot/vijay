from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
                title="Naveen",
                description="Click Here",
                input_message_contect=InputTextMessageContent(
                    message_text="""Owner of the Bot"""
                )
            )
        ],
        cecha_tine=0
    )
