from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from filters.IsPrivate import IsPrivate
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    text = [
        '<b>Список команд: </b>',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/weather - Погода в Уфе (для разработки)',
        '/timetable - получить актуальное расписание',
        '/timetable_today - получить расписание на сегодня',
        '/timetable_next - получить расписание на след. учебный день',
        '/get_list - получить список группы с порядковыми номерами',
        '/get_list_tx - получить список группы в виде сообщения',
        '/rgr - получить список вариантов группы по РГР(диффуры)',
        '/links - полезные ссылки',
        '\nЕсли отправить боту в лс сообщение "doc"\nи прикрепить к этому же сообщению докумнет,',
        'то он будет отправлен @Easy_Hunt и будет выведено соответстующее сообщение',
        '"Отправлено @Easy_Hunt"'
    ]
    await message.answer('\n'.join(text))


@rate_limit(20, 'about_me')
@dp.message_handler(Command("about_me"), IsPrivate())
async def about_me(message: types.Message):
    text = [
        '<b>Что я умею</b>',
        'Основная моя задача это ежедневная отправка в чат актульного расписания',
        'В 7:00 я выкладываю актуальное расписание на учебный день',
        'В 19:00 я выкладываю расписание на завтрашний день (если есть пары)',
        'Верхние и нижние недели тоже учитываются',
        '\nМогу отправить расписание на сегодняшний, завтрашний день, или все расписание целиком',
        'в виде сообщения или картинки',
        '\nМогу выдать список вариантов по РГР',
        '\nМогу предоставить актуальную информацию о погоде в Уфе (т.е погода на данный момент времени)',
        '\nЕсли отправить мне в лс сообщение "doc"\nи прикрепить к этому же сообщению докумнет,',
        'то я его перешлю @Easy_Hunt и выведу соответстующее сообщение',
        '"Отправлено @Easy_Hunt"',
        '\n<b>Чему я вскоре научусь:</b>',
        'Администрирование группы, совсем чуть-чуть))',
        'команды /mute для особо разговорчивых и /unmute для всех прощенных :)',
        '(ясное дело эти команды доступны только админам группы)',
        '\nИзменение расписание прямо из переписки со мной (опять же для админа только)',
        '\nВыгрузка учебников и лекций из Яндекс.Диск или другого облачного сревиса (пока не определился)',
        '\nВыдача студентам ПМИ 23 их логина и пароля от ЛК (другие получить ваш ЛК не смогут)'

    ]
    await message.answer('\n'.join(text))
