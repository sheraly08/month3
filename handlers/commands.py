from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

from handlers.keyboards import reply_keyboard, inline_keyboard, product_actions

from database import db

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

@router_commands.message(F.text == "Корзина")
async def cmd_group(message: Message):
    await message.answer(f"Добавлена в корзину!!!")

@router_commands.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!", show_alert=True)
    await callback.message.answer("Первый вопрос: Второй закон Ньютона?")



@router_commands.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f'ID этого стикера - {message.sticker.file_id}')


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgQAAxkBAANHasjwovX_4jciexabnTfLXO2mIAgAAjQaAAIwDvhTjfmtysL48cw9BA')


@router_commands.message(Command('products'))
async def get_products(message: Message):
    products = await db.get_products_db()

    staff = await db.get_staff_list()
    staff_ids = [user_id for user_id, full_name in staff]

    if not products:
        await message.answer('В базе товаров нет!')
        return
    else: 
        for name, photo, price, product_id, category, color, description in products:

            if message.from_user.id in staff_ids:
                await message.answer_photo(photo=photo, 
                                caption=f'Данные товара: \nНазвание - {name} '
                                f'\nЦена - {price} \nОписание - {description} \nКатегория - {category} \nЦвет - {color} \nАртикул - {product_id}', 
                                reply_markup=product_actions(product_id=product_id))
            else:
                await message.answer_photo(photo=photo, 
                                caption=f'Данные товара: \nНазвание - {name} '
                                f'\nЦена - {price} \nОписание - {description} \nКатегория - {category} \nЦвет - {color} \nАртикул - {product_id}')



@router_commands.message(Command('staff_list'))
async def get_staff_list(message: Message):
    staff = await db.get_staff_list()
    staff_ids = [user_id for user_id, full_name in staff]

    if message.from_user.id in staff_ids:
        for user_id, full_name in staff:
            await message.answer(f"ФИО - {full_name}, ID - {user_id}")
    else: 
        await message.answer('У вас нет доступов к данной команде!')