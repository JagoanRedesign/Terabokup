import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the Telegram bot
bot = Client("zee5_upload_bot")

# Define the command handler
@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text("Welcome to the ZEE5 Upload Bot! Send me a ZEE5 video URL and I'll upload it to Telegram.")

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

# Start the bot
bot.run()
