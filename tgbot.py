from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

from pyrogram import Client as tg

tg = Client("TG-Bot", bot_token = os.environ["BOT_TOKEN"], api_id = int(os.environ["API_ID"]), api_hash = os.environ["API_HASH"])

@tg.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=Script.START_MSG,
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


tg.run()


# Copy This And Paste Here And Replace Commands.You Can Change This Bot To Any Bot By Adding More Codes eg: Renamer bot , Group Manager Bot, etc....
