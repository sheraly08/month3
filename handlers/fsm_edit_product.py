from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import main_db
from handlers import keyboards

router_edit = Router()

class EditProduct(StatesGroup):
    field = State()
    new_value = State()

# edit:101

# edit 101

@router_edit.callback_query(F.data.startswith('edit:'))
async def edit_start(call: CallbackQuery, state: FSMContext):



    staff = await main_db.get_staff_list()
    staff_ids = [user_id for user_id, full_name in staff]
    if call.from_user.id not in staff_ids:
        await call.message.answer('У вас нет доступа к этой команде!')
        await call.answer()
        return
    

    product_id = call.data.split(":")[1]
    # print(product_id)
    await state.update_data(product_id=product_id)
    await call.message.answer('Что меняем?', reply_markup=keyboards.edit_fields)
    await call.answer()
    await state.set_state(EditProduct.field)

# field_price
# price

@router_edit.callback_query(EditProduct.field, F.data.startswith('field_'))
async def edit_field(call: CallbackQuery, state: FSMContext):
    field = call.data.removeprefix('field_')

    await state.update_data(field=field)
    await call.message.answer('Введите новое значение:')
    await call.answer()
    await state.set_state(EditProduct.new_value)


@router_edit.message(EditProduct.new_value, F.text)
async def edit_save(message: Message, state: FSMContext):
    data = await state.get_data()

    if data['field'] == 'price' and not message.text.isdigit():
        await message.answer('Цена должна быть числом. Попробуйте еще раз')
        return
    
    else:
        await main_db.update_product(field=data['field'], value=message.text, product_id=data['product_id'])
        await message.answer('Товар обновлен!')
        await state.clear()
        