from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminMessage(BoundFilter):

    async def check(self, message: types.Message):

        admins = await message.bot.get_chat_administrators(chat_id=-859544611)
        adminId = []
        for admin in admins:
            adminId.append(admin.user.id)

        if message.from_user.id in adminId:
            return True
        else:
            return False
