from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

from handlers.keyboards import reply_keyboard, inline_keyboard, inline_keyboard1

router_commands = Router()



@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот!",
        reply_markup=reply_keyboard
    )

    print(f"Пользователь {message.from_user.full_name} под ником {message.from_user.username} отправил команду /start")


@router_commands.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - привествие\n"
        "/help - список команд",
        reply_markup=inline_keyboard
    )

@router_commands.message(F.text == "Контакты")
async def cmd_info(message: Message):
    await message.answer(f"Наш телефон: 0700 370 543\n"
                         "Адрес магазина: Ул.Абая 170"
                         )

@router_commands.message(F.text == "Каталог")
async def cmd_list_product(message: Message):
    await message.answer(f"1.Macbook: 40000 сом\n"
                         "2.Iphone: 43000 сом\n"
                         "3.Powerbank: 1500 сом\n"
                         )
    
@router_commands.message(F.text == "Корзина")
async def cmd_group(message: Message):
    await message.answer(f"Добавлена в корзину!!!")

@router_commands.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!")
    await callback.message.answer("Первый вопрос: Что такое функция?",
        reply_markup=inline_keyboard1 
                                  )
    
@router_commands.callback_query(F.data == "1")
async def cmd_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Верно!")

@router_commands.callback_query(F.data == "2")
async def cmd_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Неверно\n"
                                  "Правильный ответ: Блок кода, выполняющий определённую задачу" )

@router_commands.callback_query(F.data == "3")
async def cmd_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Неверно\n"
                                  "Правильный ответ: Блок кода, выполняющий определённую задачу" )


