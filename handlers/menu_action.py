from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import datetime
from functions.today_absences import today_stuff_absences
from functions.get_users_list import get_user_id_list
from functions.report_by_params import get_report_by_params
from functions.subscribe import get_subs_unsubs
from functions.week_absences import get_weekly_absences
from keyboards.output_by_params_kb import department_kb, type_of_absence_kb, period_kb
from keyboards.subscribe_kb import get_user_id_kb
from state.output_by_params_state import ParamsState
from state.subs import IdState


async def help_info(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Приветствую, коллега!\n\n'
                                                 f'Этот бот был разработан для экономии времени. Зачем искать файл на сетевом диске, '
                                                 f'если можно нажать всего две кнопки и получить актуальную информацию?😉\n\n'
                                                 f'Бот умеет:\n'
                                                 f'- Формировать список отсутствующих на сегодняшний день - /today\n'
                                                 f'- Формировать список отсутсвующих по параметрам - /abs_param\n'
                                                 f'- Автоматически присылать список отсутвующих на текущей неделе. Рассылка осуществляется по понедельникам в 8:30.\n'
                                                 f'Чтобы подписаться  или отказаться от рассылки, используйте команду /subscribe\n\n'
                                                 f'Надеюсь, бот будет полезен Вам😊\n\n'
                                                 f'<i>со временем планируется расширение функционала</i>')


async def get_today_absences(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Отсутсвующие сегодня (<b>{datetime.date.today().strftime("%d.%m.%Y")}</b>):\n\n{today_stuff_absences()}\n')


async def weekly_absences_info(bot: Bot):
    for user_id in get_user_id_list():
        await bot.send_message(user_id, f'Список отсутствующих на текущей неделе:\n\n{get_weekly_absences()}\n')


async def get_id(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, f'Выберите действие: ', reply_markup=get_user_id_kb())
    await state.set_state(IdState.user_tg_id)
    await state.update_data(user_tg_id=message.from_user.id)


async def get_subscribe(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    await state.update_data(action=call.data)
    create_data = await state.get_data()
    print(create_data)
    await call.message.answer(f'{get_subs_unsubs(create_data)}')


async def get_params_for_report(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите вид отсутствия: ', reply_markup=type_of_absence_kb())
    await state.set_state(ParamsState.type)


async def select_type(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вид отсутствия выбран \n'
                              f'<b>Выберите отдел:</b> ')
    await state.update_data(type=call.data)
    await call.message.edit_reply_markup(reply_markup=department_kb())
    await state.set_state(ParamsState.department)


async def select_department(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Отдел выбран\n'
                              f'<b>Теперь выберите период:</b> ')
    await state.update_data(department=call.data)
    await call.message.edit_reply_markup(reply_markup=period_kb())
    await state.set_state(ParamsState.period)


async def select_period(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Период выбран.\n<b>Ожидайте отчет</b>')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.update_data(period=call.data)

    create_data = await state.get_data()
    print(create_data)

    await call.message.answer(f'<b>Отчет сформирован:</b>\n\n{get_report_by_params(create_data)}\n')
