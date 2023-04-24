import datetime
import json
from aiogram import Bot
from data.config import group_chat
from utils.Upper_Lower_week import UpperLowerweek


async def timetable_next(bot: Bot):
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

        return await bot.send_message(chat_id=group_chat, text="<b><u>Расписание на завтра</u></b>"),\
               await bot.send_message(chat_id=group_chat, text=await UpperLowerweek(), disable_notification=True), \
               await bot.send_message(chat_id=group_chat, text=timetable, disable_notification=True)
