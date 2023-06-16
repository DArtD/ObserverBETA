from data.config import group_chat
from filters.AdminMessage import AdminMessage
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command("ban"), AdminMessage())
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответов на сообщение!")
        return

    await message.bot.delete_message(chat_id=group_chat, message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=group_chat, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply(f"Пользователь {message.from_user.username} вышел покурить и не вернулся...")
