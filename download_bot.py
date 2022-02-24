

import telebot
import pytube
import os


token = '5236806659:AAGHQ71Y6nq1tvJ06Iyzcbx4b6ANJYfVOQg'

bot = telebot.TeleBot(token=token)
url = 'https://www.youtube.com/watch?v=z4LGioi816M'

current_path = os.path.abspath(os.getcwd())+'//videos'




@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, 'Я телеграм бот')


@bot.message_handler(content_types=['text'])
def send(message):
    url = message.text
    bot.send_message(message.chat.id, 'Video downloader...')
    yt = pytube.YouTube(url).streams.filter(res='720p').first().download(output_path=current_path)
    video_title = pytube.YouTube(url).title + '.mp4'
    video = open(current_path, 'rb')
    bot.send_video(message.chat.id, video)
    

print('Бот работает...')



bot.infinity_polling()

