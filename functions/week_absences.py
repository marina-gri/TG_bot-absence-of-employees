import datetime
import pandas as pd
from functions.today_absences import get_df_from_xlsx, date_format_dmy

def get_weekly_absences():
    df = get_df_from_xlsx()
    absences = ''
    week_begin = pd.to_datetime("today")
    week_end = pd.to_datetime(week_begin + datetime.timedelta(days=6))

    df = df[((df['begin'] >= week_begin) & (df['begin'] <= week_end)) | ((df['end'] >= week_begin) & (df['end'] <= week_end))]

    for i in range(len(df['name'])):
        absences += f"{df['name'].loc[df.index[i]]}\n<b>{df['type of absence'].loc[df.index[i]]}</b> с {date_format_dmy(df['begin'].loc[df.index[i]])} по {date_format_dmy(df['end'].loc[df.index[i]])}\n\n"

    if len(absences) > 0:
        print(absences)
        return absences
    else:
        return "На текущей неделе все работают 🎉"
