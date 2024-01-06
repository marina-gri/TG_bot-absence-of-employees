import asyncio
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher
from utils.commands import set_commands
from handlers.start import get_start, get_today_absences, weekly_absences_info, sec_absences_info
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text="Я включился")


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))
dp.message.register(get_today_absences, Command(commands='today'))


async def start():

    await set_commands(bot)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(weekly_absences_info, 'cron', day_of_week='0', hour='8', minute='30', kwargs={'bot': bot})
    scheduler.add_job(sec_absences_info, 'interval', seconds=15, kwargs={'bot': bot})  #быстрый тест отправки уведомлений
    scheduler.start()

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
