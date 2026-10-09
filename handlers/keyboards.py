from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")]
])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="Наш сайт", url="https://youtube.com")],
    [InlineKeyboardButton(text="Наша страница в инсте", url="https://instagram.com")],
    [InlineKeyboardButton(text="Начать игру", callback_data="quiz_start")]
])

inline_keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="1.Блок кода, выполняющий определённую задачу", callback_data="1")],
    [InlineKeyboardButton(text="2.Переменная для хранения числа", callback_data="2")],
    [InlineKeyboardButton(text="3.Файл с кодом", callback_data="3")]
    ]
)