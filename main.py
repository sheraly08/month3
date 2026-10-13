import asyncio
import logging
from handlers import commands, echo, fsm
from config import bot, dp
from database.db import create_table



async def main():
    def on_startup():
        create_table()

    on_startup()

    # регистрация обработчиков
    dp.include_router(commands.router_commands)

    dp.include_router(fsm.router_add_movie)

    

    # Обработчик на ВСЁ 
    dp.include_router(echo.router_echo)

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())