from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import state

from user.models import User_Profile

class RegisterState(state.StatesGroup):

    START = state.State()
    CHOOSE_LANGUAGE = state.State()
    SEND_PHONE_NUMBER = state.State()


def register_handlers(dp: Dispatcher):

    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply("Hi!\nI'm your bot!\nPowered by aiogram and Django.")

    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)
