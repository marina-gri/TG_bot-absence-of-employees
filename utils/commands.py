from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='today',
            description='Список отсутствующих сегодня'
        ),
        BotCommand(
            command='abs_param',
            description='Список отсутствующих по параметрам'
        ),
        BotCommand(
            command='subsribe',
            description='Подписаться на еженедельное получение списка отсутсвующих'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())