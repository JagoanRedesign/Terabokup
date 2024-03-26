#


from pyrogram import Client as Ntbots
from pyrogram import filters
from config import Config


  Ntbots=Ntbots(
       "GROUP-MEMBERS-BAN-BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

    
    
@Ntbots.on.message(filters.command(start) & filters.private)
def comand1(Ntbots, message):
    bot.send_message(message.chat.id, "hello i am a group admin bot")


    print("🎊 I AM ALIVE 🎊")
    Ntbots.run()
    
