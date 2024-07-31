from aiogram import BaseMiddleware
from aiogram.types import Update
from django.utils.translation import activate
from django.conf import settings
from typing import Callable, Dict, Awaitable, Any, Optional
from user.models import User
from asgiref.sync import sync_to_async

class I18Middleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], 
                       event: Update, 
                       data: Dict[str, Any]
                       ) -> Any:
        # Extract user ID from the event
        telegram_id = None
        if hasattr(event, 'message') and event.message:
            telegram_id = event.message.from_user.id
        elif hasattr(event, 'callback_query') and event.callback_query:
            telegram_id = event.callback_query.from_user.id
        elif hasattr(event, 'edited_message') and event.edited_message:
            telegram_id = event.edited_message.from_user.id
        # Add more checks if you need to handle more update types

        if telegram_id:
            try:
                # Retrieve the user from the database
                user = await sync_to_async(User.objects.get)(telegram_id=telegram_id)
            except User.DoesNotExist:
                user = None
        else:
            user = None

        if user is None :
            activate(settings.LANGUAGE_CODE)
        else: 

            activate(user.language)

        return await handler(event, data)
