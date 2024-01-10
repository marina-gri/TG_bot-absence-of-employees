from aiogram.utils.keyboard import InlineKeyboardBuilder
from functions.today_absences import get_df_from_xlsx
import datetime


def type_of_absence_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='отпуск', callback_data='отпуск')
    kb.button(text='больничный', callback_data='больничный')
    kb.button(text='все', callback_data='all')
    kb.adjust(2, 1)
    return kb.as_markup()


def department_kb():
    df = get_df_from_xlsx()
    kb = InlineKeyboardBuilder()
    department_list = []
    for i in range(len(df['department'])):
        if df['department'][i] in department_list:
            continue
        else:
            department_list.append(df['department'][i])
            kb.button(text=df['department'][i], callback_data=str(df['id_department'][i]))
    kb.button(text='все', callback_data='all')
    kb.adjust(1)
    return kb.as_markup()


def period_kb():
    kb = InlineKeyboardBuilder()
    current_date = datetime.date.today()
    kb.button(text='текущий месяц', callback_data=f'{current_date.month}')
    kb.button(text='следующий месяц', callback_data=f'{current_date.month + 1}')
    kb.adjust(1)
    return kb.as_markup()
