# функции для связи с бд
import sqlite3
from database import queries

#path_db = "database/sqlite3.db"
path1_db = "database/movie.db"


#def init_db():
 #   conn = sqlite3.connect(path_db)
  #  cursor = conn.cursor()
 #   cursor.execute(queries.products_table)
 #   print('DB connect')
 #   conn.commit()
 #   conn.close()

#def add_product_db(name, price, description, photo):
 #    conn = sqlite3.connect(path_db)
   #  cursor = conn.cursor()
   #  cursor.execute(queries.insert_product, (name, price, description, photo))
    
   #  conn.commit()
   #  conn.close()

def create_table():
    conn = sqlite3.connect(path1_db)
    cursor = conn.cursor()
    cursor.execute(queries.movies_table)
    print("DB connect")
    conn.commit()
    conn.close()

def add_movie_db(name, genre, rating):
    conn = sqlite3.connect(path1_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_movie, (name, genre, rating))
    conn.commit()
    conn.close()


