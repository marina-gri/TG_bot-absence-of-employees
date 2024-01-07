from aiogram.utils.keyboard import InlineKeyboardBuilder
from functions.today_absences import get_df_from_xlsx
import datetime


def type_of_absence():
    df = get_df_from_xlsx()
    kb = InlineKeyboardBuilder()
    type_of_absence_list = []
    for i in range(len(df['type of absence'])):
        if df['type of absence'][i] in type_of_absence_list:
            continue
        else:
            type_of_absence_list.append(df['type of absence'][i])
            kb.button(text=df['type of absence'][i], callback_data=df['type of absence'][i])
    kb.button(text='все', callback_data='all')
    kb.adjust(2, 1, 1)
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
    kb.button(text='текущий год', callback_data=f'{current_date.year}')
    kb.button(text='ручной ввод', callback_data='ручной ввод')
    kb.adjust(1)
    return kb.as_markup()
