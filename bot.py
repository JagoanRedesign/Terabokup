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
    await message.reply_photo(
        photo="https://graph.org/file/a5d4da221c8f34319318d.jpg",
        caption="hello 👋\n\n**I Am Group Admin Bot**\n\n**I'm Not A Fully Group Admin Bot. With Me You Can ban, unban, mute, unmute**")
    

@bot.on_message(filters.private & filters.command(["help"]))
async def help(Client, message):
    await message.reply_text("**I AM NOT A FULLY GROUP ADMIN BOT**\n\n**Admin commands:** 👇🏻\n• /ban **Ban a user.**\n• /unban **Unban a user.**\n• /mute **Mute a user.**\n• /unmute **Unmute a user.**\n")



print("🎊 I AM ALIVE 🎊")

bot.run()
