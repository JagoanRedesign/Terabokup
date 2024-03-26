#

from pyrogram import filters
from pyrogram import Client




    Client = Client(
        "GROUP-MEMBERS-BAN-BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

    print("🎊 I AM ALIVE 🎊")


@Client.on.message(filters.command(start) & filters.private)
def comand1(Client, message):
    bot.send_message(message.chat.id, "hello i am a group admin bot")

    Client.run()
