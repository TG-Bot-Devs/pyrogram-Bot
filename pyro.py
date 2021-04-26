from pyrogram import Client

api_id = # Your Value
api_hash = "YOUR_DATA"
bot_token = #bot_tokenHere

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
