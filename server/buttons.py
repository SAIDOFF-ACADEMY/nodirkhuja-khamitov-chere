from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_button = InlineKeyboardMarkup()
language_button.add(
    InlineKeyboardButton("🇺🇿 UZ", callback_data="uz"),
    InlineKeyboardButton("🇷🇺 RU", callback_data="ru"),
)