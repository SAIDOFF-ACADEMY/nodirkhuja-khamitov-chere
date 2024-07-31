'''import logging
import environ


from django.core.management.base import BaseCommand

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from server.utils.middlawares import i18n

env = environ.Env()

TOKEN = env('API_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.update.outer_middleware.register(i18n.I18Middleware())


class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        from server.handlers import register_handlers
        register_handlers(dp)
        executor.start_polling(dp, skip_updates=True)
'''


from django.core.management import BaseCommand

from server.misc import dp, bot, on_shutdown


class Command(BaseCommand):
    def handle(self, *args, **options):
        #dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        dp.run_polling(bot)


