import datetime
import json
from  utils import UpperLowerweek
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command('timetable_today'), IsPrivate())
async def timetable_today(message: types.Message):
    dt_day = datetime.datetime.today() + datetime.timedelta(hours=5)
    dt = dt_day.weekday()
    if 0 <= dt <= 4:
        timetable = ''
        with open('timetable.json', encoding="utf-8") as f:
            obj1 = f.read()
            obj = json.loads(obj1)
            if dt == 3 and await UpperLowerweek() == "<b>Нижняя неделя</b>":
                timetable += '\n' + obj["3"]["first_pair"] + '\n' + obj["3"]["second_pair"]
            else:
                for i in obj[str(dt)]:

                        timetable += '\n' + obj[str(dt)][i] + '\n'
            await message.answer(text=await UpperLowerweek())
            await message.answer(timetable)
    else:
        await message.answer("<b>Сегодня нет пар</b>")
