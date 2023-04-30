import json

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from utils.forward_messages import forward_messages

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command("rgr"), IsPrivate())
async def rgr(message: types.Message):
    count = 0
    with open('RGRgroup.json', encoding="utf-8") as f:
        list = 'Варианты по РГР (диффуры)\n'
        obj1 = f.read()
        obj = json.loads(obj1)

        for i in obj:
            count += 1
            list += f'{count}' + ': ' + obj[i] + "\n"

        await forward_messages(message)
        await dp.bot.send_document(document=open("РГР-2 (23 гр).pdf", 'rb'), chat_id=message.chat.id)
        await message.answer(list)
