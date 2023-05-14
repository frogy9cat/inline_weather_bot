from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.inline.InlineAbout import Sharing

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = f"Бот для инлайн поиска информации о погоде в городах и странах"
    await message.reply(text=text, reply_markup=Sharing)
    
