from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

start_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Контакты'
        ),
        KeyboardButton(
            text='Адрес'
        )
    ],
    [
        KeyboardButton(
            text='Меню'
        ),
        KeyboardButton(
            text='Забронировать'
        ),
        KeyboardButton(
            text='Афиша'
        )
    ]
], resize_keyboard=True, selective=True)

menu_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Меню кухни'
        ),
        KeyboardButton(
            text='Барная карта'
        )
    ]
], resize_keyboard=True, selective=True)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Наш бар ВКонтакте',
            url='https://vk.com/etobar'
        ),
        InlineKeyboardButton(
            text='Наш бар Instagram',
            url='https://www.instagram.com/thisisbar/'
        ),
        InlineKeyboardButton(
            text='Наша страница',
            url='https://thisisbar.clients.site/'
        ),

    ]
])

inline_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Барная карта',
            url='https://vk.com/s/v1/doc/-TuwsIfGJQSL8lI9d63cae-cPkbeAwQ4xe11Hw5ArIjINGrk'
        ),
        InlineKeyboardButton(
            text='Меню кухни',
            url='https://vk.com/s/v1/doc/XSNLsrD5nr5piLiG01VAtRNxCDVF66kTuxmuQa0g7flXjNLl'
        ),
        InlineKeyboardButton(
            text='Афиша',
            url='https://vk.com/etobar?z=photo-3651_457245171%2Falbum-3651_00%2Frev'
        ),

    ]
])