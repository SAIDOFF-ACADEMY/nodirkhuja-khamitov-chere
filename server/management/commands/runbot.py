from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ParseMode
import logging
import environ

env = environ.Env()

TOKEN = env('API_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        from server.handlers import register_handlers
        register_handlers(dp)
        executor.start_polling(dp, skip_updates=True)
