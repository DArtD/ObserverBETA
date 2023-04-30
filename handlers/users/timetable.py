import json
from aiogram.dispatcher.filters import Command
from aiogram import types
from utils.forward_messages import forward_messages

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command('timetable'), IsPrivate())
async def timetable(message: types.Message):
    timetable = ''

    with open('timetable.json', encoding="utf-8") as f:
        obj1 = f.read()
        obj = json.loads(obj1)

        for i in obj:
            for y in obj[i]:
                timetable += '\n' + obj[i][y] + '\n'

        await forward_messages(message)
        await message.answer(timetable)
