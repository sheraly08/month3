from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from src.keyboards import reply_keyboard, inline_keyboard, inline_keyboard1

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я твой первый бот",
        reply_markup=reply_keyboard
    )

    print(
        f"Пользователь {message.from_user.full_name} "
        f"под ником {message.from_user.username}"
    )


@router.message(Command('help'))
async def cms_help(message: Message):
    await message.answer(
        f"/start - привествие\n"
        "/help - список команд",
        reply_markup=inline_keyboard
    )

@router.message(F.text == "Контакты")
async def cmd_info(message: Message):
    await message.answer(f"Наш телефон: 0700 370 543\n"
                         "Адрес магазина: Ул.Абая 170"
                         )

@router.message(F.text == "Каталог")
async def cmd_list_product(message: Message):
    await message.answer(f"1.Macbook: 40000 сом\n"
                         "2.Iphone: 43000 сом\n"
                         "3.Powerbank: 1500 сом\n"
                         )

@router.message(F.text == "Корзина")
async def cmd_group(message):
    await message.answer(f"Добавлена в корзину  ")

@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!")
    await callback.message.answer("Первый вопрос: Что такое функция?",
        reply_markup=inline_keyboard1 
                                  )
   
@router.callback_query(F.data == "1")
async def cmd_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Верно!")

@router.callback_query(F.data == "2")
async def cmd_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Неверно\n"
                                  "Правильный ответ: Блок кода, выполняющий определённую задачу" )

@router.callback_query(F.data == "3")
async def cmd_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Неверно\n"
                                  "Правильный ответ: Блок кода, выполняющий определённую задачу" )


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")