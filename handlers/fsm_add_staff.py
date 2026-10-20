from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import main_db
from handlers import keyboards

router_add_staff = Router()

staff_code = 'x009T'

class RegisterStaff(StatesGroup):
    code = State()


@router_add_staff.message(Command('register_staff'))
async def register_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if await main_db.is_staff_db(user_id=user_id):
        await message.answer('Вы уже есть в бд!')
        return
    else:
        await message.answer("Введите код регистрации:")
        await state.set_state(RegisterStaff.code)


@router_add_staff.message(RegisterStaff.code, F.text)
async def register_check(message: Message, state: FSMContext):
    if message.text.strip() == staff_code:

        await main_db.add_staff_db(user_id=message.from_user.id, 
                              full_name=message.from_user.full_name)
        
        await message.answer("Готово! Теперь доступны взаимодействие с продуктом. ")
        
    else:
        await message.answer('Неверный код. Попробуйте снова - /register_staff')

    await state.clear()
