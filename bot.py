#




import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from config import Config
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :

    bot = Client(
        "MembersBan_Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

        #print("🎊 I AM ALIVE 🎊")
        bot.run()

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
       caption=f"""hello im admin bot"""
    )

     
    
