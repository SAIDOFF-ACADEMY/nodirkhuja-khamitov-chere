from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from asgiref.sync import sync_to_async

from product.models import Product
from user.models import User

from django.utils.translation import gettext as _

language_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 UZ"), KeyboardButton(text="🇷🇺 RU")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

async def send_contact_phone_button():
    send_contact_phone = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await sync_to_async(_)("Send my phone number"), 
                            request_contact=True)]
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    return send_contact_phone

async def send_main_button():
    main_button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await sync_to_async(_)(str("Order"))), 
             KeyboardButton(text=await sync_to_async(_)(str("My Orders")))],
            [KeyboardButton(text=await sync_to_async(_)(str('Support')))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return main_button

async def send_location_button():
    location_button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await sync_to_async(_)("Send my location"), 
                            request_location=True)],
            KeyboardButton(text=await sync_to_async(_)(str("Cancel")))
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    return location_button

async def send_confirm_button():
    confirm_button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await sync_to_async(_)(str("Confirm"))), 
             KeyboardButton(text=await sync_to_async(_)(str("Cancel")))]
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    return confirm_button

async def send_cancel_button():
    cancel_button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await sync_to_async(_)("Cancel Order"))]
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    return cancel_button


async def process_listing_product(user_telegram_id):

    products = await get_products()
    user = await get_language(user_telegram_id)

    keyboard = [[KeyboardButton(text=getattr(product, f"name_{user.language}".lower())) 
                 for product in products]]
    
    product_list = ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=True,
            one_time_keyboard=True
        )
    return product_list

@sync_to_async
def get_products():
    return list(
        Product.objects.filter(is_active=True)
    )

@sync_to_async
def get_language(user_telegram_id):
    return User.objects.get(telegram_id=user_telegram_id)