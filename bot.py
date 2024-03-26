#


from pyrogram import Client, filters
from config import Config


if __name__ == "__main__" :

    bot = Client(
        "MembersBan_Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

    
    
@Client.on_message(filters.private & filters.command(["qr_code"]))
async def qr_code(client, message):
    await message.reply_caption(
       #photo=Config.QR_PIC,
       caption=f"""hello i am admin bot"""
    )

    print("🎊 I AM ALIVE 🎊")
    bot.run()
    
