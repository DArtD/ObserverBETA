from aiogram import Bot
import datetime
import json
from utils.Upper_Lower_week import UpperLowerweek
from data.config import group_chat
from utils.get_weather import get_weather


async def timetable_today_cron(bot: Bot):
    dt_day = datetime.datetime.now() + datetime.timedelta(hours=5)
    if 0 <= dt_day.weekday() <= 4:
        timetable = ''
        with open('timetable.json', encoding="utf-8") as f:
            obj1 = f.read()
            obj = json.loads(obj1)
            for i in obj[str(dt_day)]:
                timetable += '\n' + obj[str(dt_day)][i] + '\n'
            return await bot.send_message(chat_id=group_chat, text=await get_weather(), disable_notification=True), \
                   await bot.send_message(chat_id=group_chat, text=await UpperLowerweek(), disable_notification=True), \
                   await bot.send_message(chat_id=group_chat, text=timetable, disable_notification=True)
    else:
        return await bot.send_message(chat_id=group_chat, text=await get_weather(), disable_notification=True), \
               await bot.send_message(chat_id=group_chat, text=await UpperLowerweek(), disable_notification=True), \
               await bot.send_message(chat_id=group_chat, text="<b>Сегодня нет пар</b>", disable_notification=True)
