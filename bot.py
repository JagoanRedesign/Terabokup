# Hello, this bot coding not complete

import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply


API_ID = "4888076" # use your api id
API_HASH = "8b9b8214d84305d5ba8042c93575ea84" # use your api hash
BOT_TOKEN = "6986631333:AAHJ1THDOYeWasJfJ58ARCmlyGcyCB2GPO8" # use your bot token
START_TXT = "𝐇𝐞𝐥𝐥𝐨 **{}** 👋\n\n𝐈 𝐀𝐌 𝐆𝐫𝐨𝐮𝐩 𝐀𝐝𝐦𝐢𝐧 𝐁𝐨𝐭\n\n**𝐈’𝐦 𝐍𝐨𝐭 𝐀 𝐅𝐮𝐥𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 𝐀𝐝𝐦𝐢𝐧 𝐁𝐨𝐭. 𝐖𝐢𝐭𝐡 𝐌𝐞 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐛𝐚𝐧, 𝐮𝐧𝐛𝐚𝐧, 𝐦𝐮𝐭𝐞, 𝐮𝐧𝐦𝐮𝐭𝐞**"
ABOUT_TXT = """
╭───────────⍟
├📛 **My Name** : <a href=https://t.me/MembersBan_Bot>Admin</a>
│
├📢 **Framework** : <a href=https://docs.pyrogram.org/>Pyrogram 2.0.106</a>
│
├💮 **Language** : <a href=https://www.python.org>Python 3.12.2</a>
│
├💾 **Database** : <a href=https://cloud.mongodb.com>MongoDB</a>
│
├👥 **Support Group** : <a href=https://t.me/NT_BOTS_SUPPORT>NT BOTS SUPPORT</a>
│
├🥏 **Channel** : <a href=https://t.me/NT_BOT_CHANNEL>NT BOT CHANNEL</a>
│
├🤖 **Server** : <a href=https://fly.io>Fly Paid</a>
│
├🎓 **Developer** : @yeah_new | @LISA_FAN_LK
╰───────────────⍟
"""



bot = Client(
    "Admin bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# delete button
@bot.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
		await update.message.delete()
	except:
		return

# start message
@bot.on_message(filters.private & filters.command(["start"]))
async def start(Client, update):
    await update.reply_photo(
        photo="https://graph.org/file/a5d4da221c8f34319318d.jpg",
        caption=START_TXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/NT_BOT_CHANNEL'),
      ],
      [
          InlineKeyboardButton('👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫', url='https://t.me/yeah_new'),
          InlineKeyboardButton('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/NT_BOTS_SUPPORT'),
          ],
          [
          InlineKeyboardButton('⛔️ 𝐂𝐋𝐎𝐒𝐄', callback_data='cancel')
        ]  
      ]
     ),
   )
	
# help message
@bot.on_message(filters.private & filters.command(["help"]))
async def help(Client, message):
    await message.reply_text("**I AM NOT A FULLY GROUP ADMIN BOT**\n\n**Admin commands:** 👇🏻\n• /ban **Ban a user.**\n• /unban **Unban a user.**\n• /mute **Mute a user.**\n• /unmute **Unmute a user.**\n")

# about message
@bot.on_message(filters.private & filters.command(["about"]))
async def about(Client, message):
    await message.reply_text(ABOUT_TXT, reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='⛔️ CLOSE', callback_data='cancel') ] ] ) )


# Define the ZEE5 URL handler
@bot.on_message(filters.regex(r"(https?://(?:www\.)?zee5\.com/.+)"))
async def zee5_url_handler(bot, message):
    url = message.text
    
    # Download the video from the ZEE5 URL
    video_file = download_zee5_video(url)
    
    # Upload the video to Telegram
    await bot.send_video(
        chat_id=message.chat.id,
        video=video_file,
        caption="Uploaded from ZEE5"
    )
    
    # Delete the downloaded video file
    os.remove(video_file)

# Function to download video from ZEE5 URL
def download_zee5_video(url):
    # Use requests to download the video
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the video file
        video_file = "video.mp4"  # You can use a unique filename here
        with open(video_file, "wb") as file:
            file.write(response.content)
        
        return video_file
    else:
        return None


print("🎊 I AM ALIVE 🎊")

bot.run()
