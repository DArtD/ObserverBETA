from aiogram import types
from utils.forward_messages import forward_messages

from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        await forward_messages(message)
        await message.answer(message.text)
