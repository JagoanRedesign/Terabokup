#






from pyrogram import Client, filters

if __name__ == "__main__" :

    bot = Client(
        "MembersBan_Bot",
        api_id = 4888076,
        api_hash = "8b9b8214d84305d5ba8042c93575ea84",
        bot_token = "6986631333:AAHJ1THDOYeWasJfJ58ARCmlyGcyCB2GPO8"
    )

        

@bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_text(
       caption=f"""hello im admin bot"""
    )

       print("🎊 I AM ALIVE 🎊")
       bot.run()
     
    
