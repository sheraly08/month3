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

