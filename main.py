import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from pytube import YouTube



# Configure logging
# PROXY_URL = "http://proxy.server:3128"
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN) #proxy=PROXY_URL
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    ism = message.from_user.full_name
    await message.reply(f"Assalomu aleykum {ism} xush kelibsiz \n\nMenga YouTube video linkini yuboring👇🏻")



@dp.message_handler()
async def echo(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == "https://youtu.be/" or "https://www.youtube.com/":
        await message.answer(f"Video yuklanmoqda...Iltimos kuting")
        await download_video (url, message, bot)


async def download_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True,file_extension="mp4")
    stream.get_highest_resolution().download("Videos","video")
    with open ("Videos/video", "rb") as video:
        await message.answer_video(video, caption="Video Yuklandi✅" )
        os.remove("Videos/video")
        
            
      
    






   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)