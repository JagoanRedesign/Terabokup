#



from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

bot = Client(
    "Admin bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("🎊 I AM ALIVE 🎊")

bot.run()
