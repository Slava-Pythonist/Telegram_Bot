from aiogram import Bot, Dispatcher, F
import asyncio
import logging
from aiogram.filters import CommandStart
import config
from fsm.FSMReserve import FSMReserve, get_date, cmd_reserve, get_time, get_name, get_amount, get_phone_number
from config import TOKEN, ADMIN_ID
from handlers.client_handlers import send_bar, send_food, send_concerts, cmd_contacts, cmd_locations, cmd_menu, \
    get_start, false_cmd


async def on_startup(bot: Bot):
    await bot.set_webhook(config.URL_APP)


async def on_shutdown(bot: Bot):
    await bot.set_webhook()


async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID,
                           text='<b>Бот запущен!</b>')


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID,
                           text='<b>Бот остановлен!</b>')


async def start():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(TOKEN,
              parse_mode='html')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(cmd_reserve, F.text == 'Забронировать')
    dp.message.register(get_date, FSMReserve.date)
    dp.message.register(get_time, FSMReserve.time)
    dp.message.register(get_name, FSMReserve.name)
    dp.message.register(get_amount, FSMReserve.amount)
    dp.message.register(get_phone_number, FSMReserve.phone_number)
    dp.message.register(send_bar, F.text == 'Барная карта')
    dp.message.register(send_food, F.text == 'Меню кухни')
    dp.message.register(send_concerts, F.text == 'Афиша')
    dp.message.register(cmd_contacts, F.text == 'Контакты')
    dp.message.register(cmd_locations, F.text == 'Адрес')
    dp.message.register(cmd_menu, F.text == 'Меню')
    dp.message.register(get_start, CommandStart())
    dp.message.register(false_cmd)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
