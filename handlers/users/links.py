from aiogram import types
from aiogram.dispatcher.filters import Command
from utils.forward_messages import forward_messages

from filters.IsPrivate import IsPrivate
from keyboards.inline.choice import choice
from loader import dp


@dp.message_handler(Command("Links"), IsPrivate())
async def links(message: types.Message):
    await  forward_messages(message)
    await message.answer(text="Полезные ссылки", reply_markup=choice)
