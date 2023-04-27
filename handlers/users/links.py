from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.IsPrivate import IsPrivate
from keyboards.inline.choice import choice
from loader import dp


@dp.message_handler(Command("Links"), IsPrivate())
async def links(message: types.Message):
    await message.answer(text="     Полезные ссылки", reply_markup=choice)
