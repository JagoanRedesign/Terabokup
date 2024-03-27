# Hello, this bot coding not complete

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
        caption="𝐇𝐞𝐥𝐥𝐨 👋\n\n𝐈 𝐀𝐌 𝐆𝐫𝐨𝐮𝐩 𝐀𝐝𝐦𝐢𝐧 𝐁𝐨𝐭\n\n**𝐈’𝐦 𝐍𝐨𝐭 𝐀 𝐅𝐮𝐥𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 𝐀𝐝𝐦𝐢𝐧 𝐁𝐨𝐭. 𝐖𝐢𝐭𝐡 𝐌𝐞 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐛𝐚𝐧, 𝐮𝐧𝐛𝐚𝐧, 𝐦𝐮𝐭𝐞, 𝐮𝐧𝐦𝐮𝐭𝐞**",
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 CHANNEL', url='https://t.me/NT_BOT_CHANNEL'),
      ],
      [
          InlineKeyboardButton('👨‍💻 DEVELOPER', url='https://t.me/LISA_FAN_LK'),
          InlineKeyboardButton('🌝 SOURCE', url='https://github.com/LISA-KOREA/UPLOADER-BOT-V2'),
          ]
        ]
      ),
      reply_to_message_id=update.message_id
    )

@bot.on_message(filters.private & filters.command(["help"]))
async def help(Client, message):
    await message.reply_text("**I AM NOT A FULLY GROUP ADMIN BOT**\n\n**Admin commands:** 👇🏻\n• /ban **Ban a user.**\n• /unban **Unban a user.**\n• /mute **Mute a user.**\n• /unmute **Unmute a user.**\n")



print("🎊 I AM ALIVE 🎊")

bot.run()
