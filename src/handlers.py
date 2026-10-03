from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from src.keyboards import reply_keyboard, inline_keyboard

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

@router.message(F.text == "Корзина")
async def cmd_group(message):
    await message.answer(f"Добавлена в корзину  ")

@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!", show_alert=True)
    await callback.message.answer("Первый вопрос: Второй закон ньютона")

