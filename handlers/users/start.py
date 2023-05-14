from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет! Этот бот предоставляет возможность получить информацию о погоде. Всё, что нужно сделать, это лишь написать юзер этого бота, а затем название города или страны.")
