from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from News_parser import return_news
import asyncio

bot = AsyncTeleBot('')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """
            Commands:
            /start
            /help
            /show (show news)
    """)


@bot.message_handler(commands=['show'])
async def create_message(message: Message):
    news = return_news()
    for key, value in news.items():
        await bot.reply_to(message, f'{value["Header"]}\n'
                                    f'{value["Link"]}\n')


asyncio.run(bot.polling())
