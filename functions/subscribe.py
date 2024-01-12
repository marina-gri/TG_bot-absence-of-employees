import pandas as pd

def get_subs_unsubs(subs_data: dict):
    user_id = subs_data['user_tg_id']
    action = subs_data['action']
    id_list = (pd.read_excel('/home/abs_bot/functions/users list.xlsx', sheet_name=0))['id'].tolist()
    if action == '1':
        if user_id in id_list:
            return "Вы уже подписаны на еженедельную рассылку"
        else:
            id_list.append(user_id)
            df = pd.DataFrame({'id': list(set(id_list))})
            df.to_excel(r'/home/abs_bot/functions/users list.xlsx', index=False)
            return "Вы успешно подписались на еженедельную рассылку"

    elif action == '0':
        if user_id in id_list:
            id_list.remove(user_id)
            df = pd.DataFrame({'id': id_list})
            df.to_excel(r'/home/abs_bot/functions/users list.xlsx', index=False)
            return "Вы отписались от еженедельной рассылки"
        else:
            return "Вы не были подписаны на рассылку"


