import os.path
import sqlite3 as sq
sqlite_file = 'C:/Users/blino/Documents/DB/shopProducts'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "C:/Users/blino/Documents/DB/shopProducts.db")
print(db_path)
# Поиск файла БД
# print(os.getcwd())
if os.path.exists(db_path):
    print('Found')
else:
    print('Not found')


with sq.connect(db_path) as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM products")
    # result = cur.fetchall()
    for i in cur:
        print(i)