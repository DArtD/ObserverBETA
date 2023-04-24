import datetime
import json
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command('timetable_next'), IsPrivate())
async def timetable_next(message: types.Message):
    dt_day = datetime.datetime.today() + datetime.timedelta(hours=5)
    if 4 <= dt_day.weekday() <= 6:
        dt = 0
    else:
        dt = dt_day.weekday() + 1

    timetable = ''
    with open('timetable.json', encoding="utf-8") as f:
        obj1 = f.read()
        obj = json.loads(obj1)
        for i in obj[str(dt)]:
            timetable += '\n' + obj[str(dt)][i] + '\n'
        await message.answer(timetable)
