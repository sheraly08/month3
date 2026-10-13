# sql запросы 

products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        price INTEGER,
        description TEXT,
        photo TEXT
    )
"""

insert_product = "INSERT INTO products (name, price, description, photo) VALUES (?, ?, ?, ?)" 


movies_table = """
CREATE TABLE IF NOT EXISTS movies (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
genre TEXT NOT NULL,
rating INTEGER NOT NULL

)

"""

insert_movie = "INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)"
