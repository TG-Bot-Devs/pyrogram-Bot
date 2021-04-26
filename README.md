# Tg-Bot

##### An Simple Demo Telegram Bot

<p align="left">
  <a href="https://docs.pyrogram.org/">
     <img height="30px" src="https://telegra.ph/file/4a642e823b5250c99da91.jpg">
  </a>

`Fork This Repo And Change The Repo To Any Bots
eg : Renamer Bot , YouTube Downloader Bot etc...`

### Adding Commands

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
### Change Messages

You Can Change The Messages By Replace 4Th Line ```text=Script.YOUR_MSG,``` Replace **YOUR** To Your Command Name.

### Messages

After Replace **YOUR** And Go To **Script.py** And Type Like This ```YOUR_MSG = """Your Text"""``` Replace **Your Text** To Your Cutom Message.

### Config.py

After Finishing All Deploy It `Add More Vars [⚠️Only If You Want⚠️]` . Copy This -> ```VAR_NAME = os.environ.get("VAR_NAME", "")``` Paste It On **Config.py** File.Replace `VAR_NAME`.

eg : ```SESSION_STRING = os.environ.get("SESSION_STRING", "")```

### app.json

Copy This -> ```"VAR_NAME": {
            "description": "description",
            "value": ""``` And Replace VAR_NAME To REPLACE at NAME VAR_NAME of the new VAR provided in **config.py.**

### Python

Change Python Version In `runtime.txt`.Python Updates -> [Here](https://github.com/python)

### NOW DEPLOY IT
<p align="left">
  <a href="https://heroku.com/deploy/">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a>

### Credits

[Vivek](https://github.com/Vivek-TP)

<p align="left">
  <a href="https://docs.pyrogram.org/">
     <img height="30px" src="https://telegra.ph/file/4a642e823b5250c99da91.jpg">
  </a>
