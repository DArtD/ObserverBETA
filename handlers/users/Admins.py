from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command("admins"))
async def Admins(message: types.Message):

    text = await message.bot.get_chat_administrators(chat_id=-1001844038287)
    for admin in text:
        first_name = admin.user.full_name
        userId = admin.user.id
        await message.answer(text=f"{first_name}\nid: {userId}")
