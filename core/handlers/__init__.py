from aiogram import Dispatcher
from .user_chat import setup_user_handlers


async def setup_handlers(dp: Dispatcher):
    await setup_user_handlers(dp)
