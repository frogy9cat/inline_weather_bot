from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Бот для инлайн поиска информации о погоде в городах\странах.")
    
    await message.answer(text)
