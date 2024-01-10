import pandas as pd
import calendar
from functions.today_absences import get_df_from_xlsx, date_format_dmy


def get_report_by_params(data: dict):
    type_abs = data['type']
    department = data['department']
    period = data['period']
    df = get_df_from_xlsx()
    absences = ''
    current_date = pd.to_datetime("today").date()

    if type_abs == 'отпуск' or type_abs == 'больничный':
        df = df[df['type of absence'] == type_abs]
    else:
        pass

    if department == 'all':
        pass
    else:
        df = df[df['id_department'] == int(department)]

    pd.options.mode.chained_assignment = None
    period_begin = f'{current_date.year}-{period}-1'
    period_begin = pd.to_datetime(period_begin)
    period_end = f'{current_date.year}-{period}-{calendar.monthrange(current_date.year, int(period))[1]}'
    period_end = pd.to_datetime(period_end)

    df = df[((df['begin'] >= period_begin) & (df['begin'] <= period_end)) | ((df['end'] >= period_begin) & (df['end'] <= period_end))]

    for i in range(len(df['name'])):
        absences += f"{df['name'].loc[df.index[i]]}\n<b>{df['type of absence'].loc[df.index[i]]}</b> с {date_format_dmy(df['begin'].loc[df.index[i]])} по {date_format_dmy(df['end'].loc[df.index[i]])}\n\n"

    if len(absences) > 0:
        print(absences)
        return absences
    else:
        return "по заданным параметрам нет отсутствующих"
