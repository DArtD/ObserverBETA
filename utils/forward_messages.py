from loader import dp
from aiogram import types


async def forward_messages(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
           await dp.bot.send_message(chat_id=-859544611,
                                     text=f'ID: {message.from_user.id}')
           return await dp.bot.forward_message(chat_id=-859544611,
                                               from_chat_id=message.chat.id,
                                               message_id=message.message_id)
