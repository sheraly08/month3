# функции для связи с бд
import aiosqlite
from database import queries
from config import path_db


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.products_table)
        await conn.execute(queries.products_detail_table)
        await conn.commit()
    print('База данных успешно подключена!')


async def add_product_db(name, price, description, photo, category, color, product_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product, (name, price, photo, product_id))
        await conn.execute(queries.insert_product_detail, (category, color, product_id, description))
        await conn.commit()


async def product_exists(product_id):
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.select_product_id, (product_id, ))
        return await cursor.fetchone() is not None


async def get_products_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_products)
        products = await cursor.fetchall()
    return products

# =====================================================================================
# import sqlite3
# from database import queries

# path_db = "database/sqlite3.db"

# def init_db():
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.products_table)
#     print('DB connect')
#     conn.commit()
#     conn.close()

# def add_product_db(name, price, description, photo):
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_product, (name, price, description, photo))
#     # cursor.execute(queries.insert_product, (name,))
#     conn.commit()
#     conn.close()