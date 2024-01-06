from aiogram import Bot
from aiogram.types import Message

# from keyboards.register_kb import register_keyboard
from functions.today_absences import today_stuff_absences
from functions.get_users_list import get_user_id_list


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'нажми /start')


async def get_today_absences(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Отсутсвующие:\n{today_stuff_absences()}\n')


async def weekly_absences_info(bot: Bot):
    for user_id in get_user_id_list():
        await bot.send_message(user_id, f'Отсутсвующие авто:\n{today_stuff_absences()}\n')


async def sec_absences_info(bot: Bot):
    for user_id in get_user_id_list():
        await bot.send_message(user_id, f'Отсутсвующие хоба:\n{today_stuff_absences()}\n')
