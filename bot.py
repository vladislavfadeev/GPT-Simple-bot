import openai
import asyncio
from logging.config import dictConfig

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from core.handlers import setup_handlers
from core.config.settigns import app
from core.config.logging_conf import LOGGING_CONFIG



async def main():

    openai.api_key = app.botSetting.authToken
    bot = Bot(
        token = app.botSetting.botToken,
        parse_mode=ParseMode.HTML,
    )
    dp = Dispatcher()
    await setup_handlers(dp)
    try:
        await dp.start_polling(bot, skip_updates=True,)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    dictConfig(LOGGING_CONFIG)
    asyncio.run(main())
