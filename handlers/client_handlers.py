from aiogram import Bot
from aiogram.types import Message, FSInputFile

from keyboards.client_keyboards import start_kb, inline_kb, menu_kb


# Функция get_start приветствует нового пользователя стикером, и текстом
async def get_start(message: Message, bot: Bot):
    try:
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker='CAACAgIAAxkBAAEGp8xjikpsH-7pw1tXxHTS79EBtPb2fgACBQADwDZPE_lqX5qCa011KwQ')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'<i>Здравствуйте, {message.from_user.first_name}, меня зовут Люси.\nЧем могу быть полезна?</i>',
                               reply_markup=start_kb)  # вызываем клавиатуру из модуля keyboards
        await message.delete()  # удаляем сообщение, на которое ответили
        # except перенаправляет пользователя из группы на личное общение с ботом
    except:
        await message.answer(
            text=f'<i>{message.from_user.first_name}, добро пожаловать!\n'
                 f'Я напишу вам в Личные сообщения,\nкак только вы перейдёте по ссылке:</i> '
                 f'\n"https://t.me/LucyOrwell_bot"')  # ссылка на бота


"""В данных блоках кода мы создаём функции,
 отвечающие на нажатие кнопок в клиентской части клавиатур."""


# Функция кнопки "Контакты"
# @dp.message_handler(commands=['Контакты'])
async def cmd_contacts(message: Message, bot: Bot):
    await message.answer('Контактный номер: 89001234567',
                         reply_markup=inline_kb)  # вызываем инлайн клавиатуру из модуля keyboards


# Функция кнопки "Адрес"
# @dp.message_handler(commands=['Адрес'])
async def cmd_locations(message: Message, bot: Bot):
    await message.answer('Санкт-Петербург\nВладимирский пр-т 14')
    await bot.send_location(chat_id=message.from_user.id,  # Эта часть кода отвечает за отправку геолокации
                            latitude=59.92972518838155,  # latitude - широта
                            longitude=30.348554327592936)  # longitude - долгота


# Функция кнопки "Меню"
# @dp.message_handler(commands=['Меню'])
async def cmd_menu(message: Message, bot: Bot):
    await message.reply('Вас интересуют напитки или наша кухня?',
                        reply_markup=menu_kb)


# Функция кнопки "Барная карта"
async def send_bar(message: Message, bot: Bot):
    photo_bar = FSInputFile(r'/home/slava/Documents/Lucy/images/bar.jpg')  # Указываем адрес фотографии для её отправки
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_bar)


# Функция кнопки "Меню кухни"
async def send_food(message: Message, bot: Bot):
    photo_food = FSInputFile(r'/home/slava/Documents/Lucy/images/food.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_food)


# Функция кнопки "Афиша"
async def send_concerts(message: Message, bot: Bot):
    photo_food = FSInputFile(r'/home/slava/Documents/Lucy/images/concerts.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_food)


# Данная функция отлавливает любые сообщения, не являющиеся командами для бота,
# в таком случае пользователю открывается стартовое меню
async def false_cmd(message: Message, bot: Bot):
    await message.answer(
        f'Прошу прощения, {message.from_user.username}, я не понимаю вашу просьбу, вот список команд: ',
        reply_markup=start_kb)
