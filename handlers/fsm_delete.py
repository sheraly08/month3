from aiogram import Router, F
from aiogram.types import CallbackQuery
from database import db
from handlers import keyboards


router_delete = Router()


@router_delete.callback_query(F.data.startswith('delete:'))
async def delete_start(call: CallbackQuery):
    if not await db.is_staff_db(user_id=call.from_user.id):
        await call.answer('У вас нет доступа к этой команде!', show_alert=True)
        return

    product_id = call.data.split(':')[1]
    await call.message.edit_reply_markup(reply_markup=keyboards.confirm_delete(product_id))
    await call.answer('Точно удалить?')


@router_delete.callback_query(F.data.startswith('delete_yes:'))
async def delete_confirm(call: CallbackQuery):
    if not await db.is_staff_db(user_id=call.from_user.id):
        await call.answer('У вас нет доступа к этой команде!', show_alert=True)
        return

    product_id = call.data.split(':')[1]
    if await db.delete_product_db(product_id=product_id):
        await call.message.delete()
        await call.answer(f'Товар {product_id} удалён!', show_alert=True)
    else:
        await call.answer('Такого товара уже нет в базе', show_alert=True)



@router_delete.callback_query(F.data.startswith('delete_no:'))
async def delete_cancel(call: CallbackQuery):
    product_id = call.data.split(':')[1]
    await call.message.edit_reply_markup(reply_markup=keyboards.product_actions(product_id))
    await call.answer('Удаление отменено')
