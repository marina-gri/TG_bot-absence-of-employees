import pandas as pd


def get_user_id_list():
    id_list = (pd.read_excel('/home/abs_bot/functions/users list.xlsx', sheet_name=0))['id'].tolist()
    return id_list