import datetime
import json
from aiogram import Bot
from data.config import group_chat
from utils.Upper_Lower_week import UpperLowerweek


async def timetable_next(bot: Bot):
    dt_day = datetime.datetime.today() + datetime.timedelta(hours=5)
    if 4 <= dt_day.weekday() <= 6:
        dt = 0
        check = True
    else:
        dt = dt_day.weekday() + 1
        check = False

    timetable = ''
    with open('timetable.json', encoding="utf-8") as f:
        obj1 = f.read()
        obj = json.loads(obj1)
        if dt == 3 and await UpperLowerweek() == "<b>Верхняя неделя</b>":
            timetable += '\n' + obj["3"]["first_pair"] + '\n' \
                         + obj["3"]["second_pair"] + '\n' + obj["3"]["third_pair"]
        else:
            for i in obj[str(dt)]:
                timetable += '\n' + obj[str(dt)][i] + '\n'

        return await bot.send_message(chat_id=group_chat, text="<b><u>Расписание на завтра</u></b>"),\
               await bot.send_message(chat_id=group_chat, text=await UpperLowerweek(nx_week=check), disable_notification=True), \
               await bot.send_message(chat_id=group_chat, text=timetable, disable_notification=True)
