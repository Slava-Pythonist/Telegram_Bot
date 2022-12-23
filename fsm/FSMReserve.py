from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from config import ADMIN_ID


class FSMReserve(StatesGroup):
    date = State()
    time = State()
    name = State()
    amount = State()
    phone_number = State()


async def cmd_reserve(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{message.from_user.first_name}, чтобы забронировать места,\n'
                                f'прошу указать необходимые данные:'
                                f'\nНа какую дату вас записать?')
    await state.set_state(FSMReserve.date)


async def get_date(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Записали на {message.text}\nК какому времени вас ожидать?.')
    await state.update_data(date=message.text)
    await state.set_state(FSMReserve.time)


async def get_time(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Ожидаем вас к {message.text},\nУкажите контактное имя.')
    await state.update_data(time=message.text)
    await state.set_state(FSMReserve.name)


async def get_name(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Записываю на имя, {message.text}\nСейчас укажите точное количество ваших спутников.'
                         f'\nМы бы не хотели, чтобы кто-то был вынужден стоять.')
    await state.update_data(name=message.text)
    await state.set_state(FSMReserve.amount)


async def get_amount(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Итак, мы ждём {message.text} персон.\nНаконец, введите контактный номер телефона.')
    await state.update_data(amount=message.text)
    await state.set_state(FSMReserve.phone_number)


async def get_phone_number(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Контактный номер {message.text}\n'
                         f'Спасибо, {message.from_user.first_name}, ваш стол забронирован.\n'
                         f'Должна вас уведомить, что в случае опаздания бронь снимается через 15 минут, '
                         f'по-этому убедительно прошу вас позвонить в случае непредвиденных обстоятельств воизбежание неприятных ситуаций.\n'
                         f'Спасибо за понимание, мы поможем вам хорошо провести время 😊 ')
    await state.update_data(phone_number=message.text)
    context_data = await state.get_data()
    await bot.send_message(ADMIN_ID,
                           f'Сохранение данных:'
                           f'{str(context_data)}')
    date = context_data.get('date')
    time = context_data.get('time')
    name = context_data.get('name')
    data_user = f'Данные о бронировании:\n' \
                f'Дата: {date}\n' \
                f'Время: {time}\n' \
                f'Имя: {name}'
    await message.answer(data_user)
    await state.clear()