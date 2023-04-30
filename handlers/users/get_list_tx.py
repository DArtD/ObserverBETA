import json
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters.IsPrivate import IsPrivate
from utils.forward_messages import forward_messages
from loader import dp


@dp.message_handler(Command('get_list_tx'), IsPrivate())
async def get_list_tx(message: types.Message):
    count = 0
    with open('group.json', encoding="utf-8") as f:
        list = ''
        obj1 = f.read()
        obj = json.loads(obj1)

        for i in obj:
            count += 1
            list += f'{count}' + ': ' + obj[i] + "\n"

        await forward_messages(message)
        await message.answer(list)
