#






from pyrogram import Client, filters
from config import Config



    Client = Client(
        "MembersBan_Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

        

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
       caption=f"""hello im admin bot"""
    )

       print("🎊 I AM ALIVE 🎊")
       Client.run()
     
    
