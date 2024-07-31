from aiogram import types, Router, F
from aiogram.fsm import state
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from asgiref.sync import sync_to_async

from user.models import User
from server.buttons import (
                            language_button, 
                            send_contact_phone_button, 
                            send_main_button, 
                            process_listing_product,
                            send_location_button,
                            send_cancel_button,
                            send_confirm_button
                            )

from server.filters.states import Registeration, Order
from product.models import FreeProduct

from django.utils.translation import gettext as _

router = Router()



class MainMenu(state.StatesGroup):

    ORDER = state.State()
    MY_ORDER = state.State()
    SUPPORT = state.State()



@router.message(Command('start'))
async def send_welcome(message: types.Message, state: FSMContext):
        try:
            await sync_to_async(User.objects.get)(telegram_id=message.from_user.id)
            greeting_text = await sync_to_async(_)(str("Hello"))
            main_button = await send_main_button()
            await message.answer(greeting_text, reply_markup=main_button)
        except User.DoesNotExist:
            await state.set_state(Registeration.CHOOSE_LANGUAGE)
            await message.answer(("Assalomu aleykum, Привет"))
            await message.answer(
                  ("Tilni tanlang, Выберите язык"), 
                  reply_markup=language_button
                  )


@router.message(Registeration.CHOOSE_LANGUAGE, 
                lambda message: message.text in ["🇺🇿 UZ", "🇷🇺 RU"])
async def process_language(message: types.Message, state: FSMContext):
        
        user_language = 'uz' if message.text == "🇺🇿 UZ" else 'ru'
        await state.update_data(language=user_language)
        user_data = await state.get_data()
        await state.set_state(Registeration.NAME)
        await message.answer(
              await sync_to_async(_)
              (str("What is your name?"))
              )

@router.message(Registeration.CHOOSE_LANGUAGE, 
                lambda message: message.text not in ["🇺🇿 UZ", "🇷🇺 RU"])
async def process_language(message: types.Message, state: FSMContext):
        await message.answer(
              ("Tilni tanlang, Выберите язык"), 
              reply_markup=language_button
              )


@router.message(Registeration.NAME)
async def process_language(message: types.Message, state: FSMContext):
        await state.update_data(full_name=message.text)
        phone_button = await send_contact_phone_button()
        await message.reply(
              await sync_to_async(_)
              (str("What is your phone number?")), 
              reply_markup=phone_button
              )
        await state.set_state(Registeration.SEND_PHONE_NUMBER)


@router.message(Registeration.SEND_PHONE_NUMBER)
async def process_phone_number(message: types.Message, state: FSMContext):
        if message.content_type ==  types.ContentType.CONTACT:
            await state.update_data(phone_number=message.contact.phone_number)
            data = await state.get_data()
            user = await sync_to_async(User.objects.get)(telegram_id=message.from_user.id)
            user.phone_number = data.get('phone_number')
            user.full_name = data.get('full_name')
            await sync_to_async(user.save)()
            main_button = await send_contact_phone_button()
            await message.answer(
                  await sync_to_async(_)
                  (str("Thank you for the information. Registration complete!")), 
                  reply_markup=main_button)
            await state.clear()
        else:
            await message.answer(('Please send your phone number'))



# MAIN MENU
@router.message(lambda message: message.text in 'Buyurtma berish')
async def start_order(message: types.Message, state: FSMContext): 
    products_list = await process_listing_product(message.from_user.id)
    await message.answer(await sync_to_async(_)(str("Please choose product")), 
                         reply_markup=products_list)
    await state.set_state(Order.CHOOSE_PRODUCT)


@router.message(Order.CHOOSE_PRODUCT)
async def process_order_choose_product(message: types.Message, state: FSMContext):
        await state.update_data(product=message.text)
        cancel_button = await send_cancel_button()
        await message.reply(
              await sync_to_async(_)
              ("Quantity of product (only number)?"), 
              reply_markup=cancel_button
              )
        await state.set_state(Order.QUANTITY)


@router.message(Order.QUANTITY)
async def process_order_quantity(message: types.Message, state: FSMContext):
        cancel_button = await send_cancel_button()
        try: 
              quantity = int(message.text)
        except: 
              return await message.reply(await sync_to_async(_)
                                           ("Please enter only a valid number."), 
                                           reply_markup=cancel_button)
        data = await state.get_data()
        product = data.get('product')       
        free_count = await sync_to_async(FreeProduct.discount)(quantity, product)
        await state.update_data(quantity=int(message.text))
        await state.update_data(free_count=free_count)
        location_button = await send_location_button()
        await message.answer(
                             await sync_to_async(_)
                             ("Please send your location"), 
                             reply_markup=location_button
                             )
        await message.answer(reply_markup=cancel_button)
        await state.set_state(Order.LOCATION)


@router.message(Order.LOCATION)
async def process_order_location(message: types.Message, state: FSMContext):
        if message.content_type ==  types.ContentType.LOCATION:
            confirm_button = await send_confirm_button()
            state.update_data(latitude=message.location.latitude)
            state.update_data(longitude=message.location.longitude)
            await message.answer(
                    await sync_to_async(_)
                    ("Do you confirm order?"), 
                    reply_markup=confirm_button
                    )
            await state.set_state(Order.CONFIRM)
        else:
            await message.answer(
                  await sync_to_async(_)
                  ('Please send your location')
                  )


            

@router.message(Order.CONFIRM)
async def process_confirm(message: types.Message, state: FSMContext):
      ...



@router.message(Order.LOCATION, F.text.casefold() == "Buyurtmani bekor qilish")
async def process_dont_like_write_bots(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    main_button = await send_main_button()
    await message.answer(
        "Not bad not terrible.\nSee you soon.",
        reply_markup=main_button,
    )



    







