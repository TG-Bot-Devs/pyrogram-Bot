# Tg-Bot

##### An Simple Demo Telegram Bot

######## Fork This Repo And Change The Repo To Any Bots eg : Renamer Bot , YouTube Downloader Bot etc...

You Can Add More Commands On This Repo.

Copy This And Paste On tgbot.py And Replace The >Text< To Your Command.👇🏻 And You Can Add More Modules.

`````
@tg.on_message(filters.command('text') & filters.private)
async def text(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("text", url="https://example.com"),
                    InlineKeyboardButton("text", url="https://example.com")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )
`````
