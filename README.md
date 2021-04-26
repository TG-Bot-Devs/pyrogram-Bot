# Tg-Bot

##### An Simple Demo Telegram Bot

`Fork This Repo And Change The Repo To Any Bots
eg : Renamer Bot , YouTube Downloader Bot etc...`

You Can Add More Commands On This Repo.

Copy This And Paste On **tgbot.py** And Replace The **Text** To Your Command.👇🏻 And You Can Add More Modules.
`````
@tg.on_message(filters.command('text') & filters.private)
async def text(client, message):
    await message.reply_text(
        text=Script.YOUR_MSG,
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
You Can Change The Messages By Replace 4Th Line ```text=Script.YOUR_MSG,``` Replace **YOUR** To Your Command Name.

After Replace **YOUR** And Go To **Script.py** And Type Like This ```YOUR_MSG = """Your Text"""``` Replace **Your Text** To Your Cutom Message.

After Finishing All Deploy It `Add More Vars If You Want` . Go To confing.py And 

##### Credits

[Vivek](https://github.com/Vivek-TP)

[Pyrogram](https://github.com/Pyrogram)
