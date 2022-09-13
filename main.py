from venv import create
from mysql.connector import connect, Error
from getpass import getpass
import requests
import pymysql
from flask import Flask, render_template

app = Flask(__name__)

# connection = connect(
#     host="localhost",
#     user=("root"),
#     password=("Altctrldelete666!"),
#     database="shop")

# try:
#     with connection.cursor() as cursor:
#         cursor.execute(requests.create_shop_table_query)
#         cursor.execute(requests.insert_product_query)
#         cursor.execute(requests.insert_product_query2)
#         # cursor.execute(requests.show_table_query)
#         # cursor.execute(requests.check_table_query)
#         # result = cursor.fetchall()
#         # for row in result:
#         #     print(row)
#         connection.commit()
# except Error as e:
#     print(e)

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Altctrldelete666!',
    db='shop',
    charset='utf8'
)

@app.route('/')
def first_page():
    cur = conn.cursor()
    cur.execute(requests.check_table_query)
    content = cur.fetchall()

    cur.execute(requests.fields_table_query)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]

    return render_template('first_page.html', labels=labels, content=content)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
