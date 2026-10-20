# sql запросы 

products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        price INTEGER,
        photo TEXT,
        product_id INTEGER NOT NULL UNIQUE
    )
"""


insert_product = "INSERT INTO products (name, price, photo, product_id) VALUES (?, ?, ?, ?)"



products_detail_table = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        color TEXT,
        product_id INTEGER NOT NULL UNIQUE,
        description TEXT
    )
"""

insert_product_detail = "INSERT INTO products_detail (category, color, product_id, description) VALUES (?, ?, ?, ?)" 

# products.product_id = products_detail.product_id 

select_product_id = "SELECT 1 FROM products WHERE product_id = ?"


get_products = """
SELECT p.name, p.photo, p.price, p.product_id, pd.category, pd.color, pd.description
FROM products p
INNER JOIN products_detail pd on p.product_id = pd.product_id
"""


update_product = 'UPDATE {table} SET {field} = ? WHERE product_id = ?'


create_staff_table = """
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        full_name TEXT,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

check_staff = 'SELECT 1 FROM staff WHERE user_id = ?'

insert_staff = "INSERT INTO staff (user_id, full_name) VALUES (?, ?)"

get_staff_list = 'SELECT user_id, full_name FROM staff'


delete_product = 'DELETE FROM {table} WHERE product_id = ?'



# ===================== ДЗ: фильмы (своя база movie.db) =====================

# 1-я таблица: основное о фильме
movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rating INTEGER NOT NULL
    )
"""

# 2-я таблица: подробности, связаны с movies через movie_id
movies_detail_table = """
    CREATE TABLE IF NOT EXISTS movies_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER NOT NULL UNIQUE,
        genre TEXT NOT NULL,
        year INTEGER,
        description TEXT
    )
"""

insert_movie = "INSERT INTO movies (name, rating) VALUES (?, ?)"

insert_movie_detail = "INSERT INTO movies_detail (movie_id, genre, year, description) VALUES (?, ?, ?, ?)"

# movies.id = movies_detail.movie_id
get_movies = """
SELECT m.id, m.name, m.rating, md.genre, md.year, md.description
FROM movies m
INNER JOIN movies_detail md ON m.id = md.movie_id
"""
