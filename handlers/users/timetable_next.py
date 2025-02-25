# import datetime
# import json
from aiogram.dispatcher.filters import Command
from aiogram import types
# from utils.forward_messages import forward_messages

from filters.IsPrivate import IsPrivate
from loader import dp
# from utils import UpperLowerweek


@dp.message_handler(Command('timetable_next'), IsPrivate())
async def timetable_next(message: types.Message):
    await message.answer(text="<b><u>Пары закончились</u></b>")

    # dt_day = datetime.datetime.today() + datetime.timedelta(hours=5)
    #
    # if 4 <= dt_day.weekday() <= 6:
    #     dt = 0
    #     check = True
    # else:
    #     dt = dt_day.weekday() + 1
    #     check = False
    #
    # timetable = ''
    #
    # with open('timetable.json', encoding="utf-8") as f:
    #     obj1 = f.read()
    #     obj = json.loads(obj1)
    #
    #     if dt == 3 and await UpperLowerweek(nx_week=check) == "<b>Нижняя неделя</b>":
    #         timetable += '\n' + obj["3"]["first_pair"] + '\n' + obj["3"]["second_pair"]
    #
    #     else:
    #         for i in obj[str(dt)]:
    #             timetable += '\n' + obj[str(dt)][i] + '\n'
    #
    #     await forward_messages(message)
    #     await message.answer(text=await UpperLowerweek(nx_week=check))
    #     await message.answer(timetable)
