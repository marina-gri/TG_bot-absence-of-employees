from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message


def get_user_id_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Подписаться', callback_data='1')
    kb.button(text='Отписаться', callback_data='0')
    kb.adjust(1)
    return kb.as_markup()

