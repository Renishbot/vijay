from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InlineTextMessageContect 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
                title="Naveen",
                description="Click Here",
                input_message_contect=InlineTextMessageContect(
                    message_text="""Owner of the Bot"""
                )
            )
        )
