from loader import dp
from aiogram import types


async def forward_messages(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        return await dp.bot.send_message(chat_id=-859544611, text=f"{message.from_user.full_name, message.from_user.id}"
                                                                  f"\n'{message.text}'")

