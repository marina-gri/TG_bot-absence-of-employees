from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
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
            command='subscribe',
            description='Подписаться на еженедельное получение списка отсутсвующих'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())