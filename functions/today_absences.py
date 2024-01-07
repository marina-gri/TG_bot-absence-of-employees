import datetime
import pandas as pd
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_df_from_xlsx():
    """Читаем файл, формируем DataFrame"""
    df = pd.read_excel('functions/staff absence.xlsx', sheet_name=0, header=0)
    return df


def date_format_dmy(date):
    convert_date = date.strftime('%d.%m.%Y')
    return convert_date


def today_stuff_absences():
    df = get_df_from_xlsx()

    """ Конвертируем дату из datetime64 в datetime """
    df['begin_new'] = df['begin'].map(datetime.datetime.date)
    df['end_new'] = df['end'].map(datetime.datetime.date)

    """ Формируем список отсутствующих сегодня """
    absences = ''
    for i in range(len(df['name'])):
        if df['begin_new'][i] <= pd.to_datetime('today').date() <= df['end_new'][i]:
            absences += f"{df['name'][i]} <b>{df['type of absence'][i]}</b> с {date_format_dmy(df['begin'][i])} по {date_format_dmy(df['end'][i])}\n"
        else:
            continue

    return absences



