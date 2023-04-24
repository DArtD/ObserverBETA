from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from filters.IsPrivate import IsPrivate
from loader import dp

@dp.message_handler(Command("id"), IsPrivate())
async def chat_id(message: types.Message):
    await message.answer(f"ID чата: {message.chat.id}")