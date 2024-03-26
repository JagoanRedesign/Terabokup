#

from pyrogram import filters
from pyrogram import Client




    Client = Client(
        "GROUP-MEMBERS-BAN-BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)

    print("🎊 I AM ALIVE 🎊")

    Client.run()
