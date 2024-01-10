from aiogram.fsm.state import StatesGroup, State


class IdState(StatesGroup):
    user_tg_id = State()
    action = State()
