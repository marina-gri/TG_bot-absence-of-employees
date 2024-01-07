from aiogram.fsm.state import StatesGroup, State


class ParamsState(StatesGroup):
    type = State()
    department = State()
    staff = State()
    period = State()


