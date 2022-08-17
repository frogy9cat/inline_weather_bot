from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.inline import InlineAbout

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(f"Бот для инлайн поиска информации о погоде в городах\странах.\n\nСоздатель: @frogy_cat", reply_markup=InlineAbout)
