import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.filters import Command

from handlers.menu_action import help_info, get_today_absences, weekly_absences_info, get_params_for_report, select_type, select_department, select_period, get_id, get_subscribe
from state.output_by_params_state import ParamsState
from state.subs import IdState
from utils.commands import set_commands

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text="Я включился")


dp.startup.register(start_bot)
dp.message.register(help_info, Command(commands='help'))
dp.message.register(get_today_absences, Command(commands='today'))
dp.message.register(get_id, Command(commands='subscribe'))
dp.callback_query.register(get_subscribe, IdState.user_tg_id)

dp.message.register(get_params_for_report, Command(commands='abs_param'))
dp.callback_query.register(select_type, ParamsState.type)
dp.callback_query.register(select_department, ParamsState.department)
dp.callback_query.register(select_period, ParamsState.period)


async def start():

    await set_commands(bot)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(weekly_absences_info, 'cron', day_of_week='0', hour='8', minute='30', kwargs={'bot': bot})
    # scheduler.add_job(weekly_absences_info, 'interval', seconds=30, kwargs={'bot': bot})  #быстрый тест отправки уведомлений
    scheduler.start()

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
