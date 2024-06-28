from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply("Hi!\nI'm your bot!\nPowered by aiogram and Django.")

    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)
