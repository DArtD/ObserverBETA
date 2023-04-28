from aiogram import Bot
import datetime
import json
from utils.Upper_Lower_week import UpperLowerweek
from data.config import group_chat
from utils.get_weather import get_weather


async def timetable_today_cron(bot: Bot):

    dt_day = datetime.datetime.today() + datetime.timedelta(hours=5)
    dt = dt_day.weekday()
    if 0 <= dt <= 5:

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

                return await bot.send_message(chat_id=group_chat, text=await get_weather(), disable_notification=True), \
                       await bot.send_message(chat_id=group_chat, text=await UpperLowerweek(), disable_notification=True), \
                       await bot.send_message(chat_id=group_chat, text=timetable, disable_notification=True)

        else:
            return await bot.send_message(chat_id=group_chat, text=await get_weather(), disable_notification=True), \
                   await bot.send_message(chat_id=group_chat, text=await UpperLowerweek(), disable_notification=True), \
                   await bot.send_message(chat_id=group_chat, text="<b>Сегодня нет пар</b>", disable_notification=True)

    else:
        return
