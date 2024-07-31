import environ

from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage


from django.conf import settings

from server.utils.middlewares import i18n
from server.handlers import router


env = environ.Env()

TOKEN = env('API_TOKEN')

dp = Dispatcher(storage=MemoryStorage())
bot_session = AiohttpSession()

bot = Bot(token=TOKEN)

dp.include_router(router)
dp.update.outer_middleware.register(i18n.I18Middleware())

async def on_shutdown():
    await bot_session.close()