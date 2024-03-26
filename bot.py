#


from pyrogram import Client, filters
from config import Config


if __name__ == "__main__" :

    bot = Client(
        "MembersBan_Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

    
    
@bot.on.message(filters.command(start) & filters.private)
def comand1(bot, message):
    bot.send_message(message.chat.id, "hello i am a group admin bot")


    print("🎊 I AM ALIVE 🎊")
    bot.run()
    
