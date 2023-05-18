import json
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters.IsPrivate import IsPrivate
from loader import dp
from utils.forward_messages import forward_messages


@dp.message_handler(Command("exams"), IsPrivate())
async def exams(message: types.Message):
    with open('exams.json', encoding="utf-8") as f:
        obj1 = f.read()
        obj = json.loads(obj1)
        await message.answer(obj["exams"])

    await forward_messages(message)