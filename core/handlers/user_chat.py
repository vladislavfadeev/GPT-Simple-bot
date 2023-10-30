import logging
from types import NoneType
import openai

from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from core.config.constants import SYS_DESCRIPTION


async def start(message: Message):
    await message.answer(
        text=(
            "Привет! Я ChatGPT-3.5 turbo. 🤖\n"
            "Чем могу быть полезна? Просто напишите свой вопрос."
        )
    )


async def clear_cache(message: Message, state: FSMContext):
    await state.update_data(context=[])
    await message.answer(text=("Контекст диалога успешно удален!"))


async def some_message(message: Message, bot: Bot, state: FSMContext):
    data: dict = await state.get_data()
    context: list | NoneType = data.get("context")
    messages: list = []

    if not context:
        context: list = []

    answer: Message = await bot.send_message(
        message.from_user.id, text="🤖 Размышляю над ответом.."
    )
    context.append({"role": "user", "content": message.text})
    messages.extend(SYS_DESCRIPTION)
    messages.extend(context)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature=1.1, stream=True
        )
        chunk_text = ""
        # перебираем поток событий
        for chunk in response:
            chunk_data: dict = chunk["choices"][0]["delta"]
            chunk_text += chunk_data.get("content", "")
    except openai.error.RateLimitError:
        await answer.edit_text(
            text="В настоящий момент модель перегружена. Повторите запрос."
        )
    except openai.error.APIConnectionError:
        await answer.edit_text(text="Ошибка соединения. Повторите запрос.")
    except Exception as e:
        logging.exception(e)
        await answer.edit_text(
            text="Вероятно контекст переполнен. Попробуйте его очистить, нажав на соответствующую команду в меню."
        )
    else:
        try:
            await answer.edit_text(text=chunk_text)
        except:
            pass
        if len(context) >= 7:
            context.pop(0)
            context.append({"role": "assistant", "content": chunk_text})
            await state.update_data(context=context)
        else:
            context.append({"role": "assistant", "content": chunk_text})
            await state.update_data(context=context)


async def setup_user_handlers(dp: Dispatcher):
    """
    Registry callback handlers.
    """
    dp.message.register(
        start,
        Command(
            commands=["start"],
        ),
    )
    dp.message.register(
        clear_cache,
        Command(
            commands=["clear_cache"],
        ),
    )
    dp.message.register(some_message, F.text)
