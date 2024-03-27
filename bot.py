# Hello, this bot coding not complete

from pyrogram import Client, filters


API_ID = "4888076"
API_HASH = "8b9b8214d84305d5ba8042c93575ea84"
BOT_TOKEN = "6986631333:AAHJ1THDOYeWasJfJ58ARCmlyGcyCB2GPO8"

bot = Client(
    "Admin bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@bot.on_message(filters.private & filters.command(["start"]))
async def start(Client, message):
    await message.reply_text("hello,\nI Am group Admin Bot")
    

@bot.on_message(filters.private & filters.command(["help"]))
async def help(Client, message):
    await message.reply_text("I AM NOT A FULLY GROUP ADMIN BOT\nI'M ONLY BAN UNBAN MUTE UNMUTE BOT")



print("🎊 I AM ALIVE 🎊")

bot.run()
