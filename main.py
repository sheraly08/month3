import asyncio
import logging
from handlers import commands, echo, fsm_add_product, fsm_edit_product, fsm_add_staff, fsm_delete, fsm_movie_hw
from config import bot, dp
from database import main_db


# Вызывается один раз при старте бота
async def on_startup():
    await main_db.create_table()


async def main():
    await main_db.init_db()
    # регистрация обработчиков
    dp.include_router(commands.router_commands)
    dp.include_router(fsm_add_product.router_add_product)
    dp.include_router(fsm_edit_product.router_edit)
    dp.include_router(fsm_add_staff.router_add_staff)
    dp.include_router(fsm_delete.router_delete)
    dp.include_router(fsm_movie_hw.router_add_movie)
    

    # Обработчик на ВСЁ 
    dp.include_router(echo.router_echo)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())