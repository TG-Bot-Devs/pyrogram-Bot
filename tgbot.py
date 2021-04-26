from pyrogram import filters
from pyrogram import Client as tg
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config

@tg.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Souce", url="https://github.com/vivek-tp/Tg-Bot"),
                    InlineKeyboardButton("Support", url="https://t.me/OpensourceTG")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )

# Copy This And Paste Here And Replace Commands.You Can Change This Bot To Any Bot By Adding More Codes eg: Renamer bot , Group Manager Bot, etc....
