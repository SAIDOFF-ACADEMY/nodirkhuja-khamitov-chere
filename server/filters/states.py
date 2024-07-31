from aiogram.fsm.state import StatesGroup, State


class Registeration(StatesGroup):

    CHOOSE_LANGUAGE   = State()
    NAME              = State()
    SEND_PHONE_NUMBER = State()


class Order(StatesGroup):

    CHOOSE_PRODUCT = State()
    QUANTITY       = State()
    LOCATION       = State()
    CONFIRM        = State()