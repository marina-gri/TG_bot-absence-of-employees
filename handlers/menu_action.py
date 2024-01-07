from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from functions.today_absences import today_stuff_absences
from functions.get_users_list import get_user_id_list
from functions.report_by_params import get_report_by_params
from keyboards.output_by_params_kb import department_kb, type_of_absence, period_kb
from state.output_by_params_state import ParamsState

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'нажми /start')


async def get_today_absences(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Отсутсвующие:\n{today_stuff_absences()}\n')


async def weekly_absences_info(bot: Bot):
    for user_id in get_user_id_list():
        await bot.send_message(user_id, f'Отсутсвующие авто:\n{today_stuff_absences()}\n')


async def seconds_absences_info(bot: Bot):
    for user_id in get_user_id_list():
        await bot.send_message(user_id, f'Отсутсвующие хоба:\n{today_stuff_absences()}\n')


async def get_params_for_report(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите вид отсутствия: ', reply_markup=type_of_absence())
    await state.set_state(ParamsState.type)


async def select_type(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вид отсутствия выбран \n'
                              f'Выберите отдел: ')
    await state.update_data(type=call.data)
    await call.message.edit_reply_markup(reply_markup=department_kb())
    await state.set_state(ParamsState.department)


async def select_department(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Выбран отдел {call.data}\n'
                              f'Выберите период: ')
    await state.update_data(department=call.data)
    await call.message.edit_reply_markup(reply_markup=period_kb())
    await state.set_state(ParamsState.period)


async def select_period(call: CallbackQuery, state: FSMContext, bot: Bot):
    await call.message.answer(f'Период выбран. Ожидайте отчет')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.update_data(period=call.data)

    create_data = await state.get_data()
    print(create_data)

    await call.message.answer(f'Отчет сформирован:\n{get_report_by_params(create_data)}\n')