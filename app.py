from flask import Flask
from flask import render_template
import sqlite3 as sl

con = sl.connect('database.db')

# подготавливаем  запрос
sql = 'INSERT INTO orders (product, amount, client_id) values(?, ?, ?)'
# указываем данные для запроса
data = [
    ('табурет', 2, 1)
]
# добавляем запись в таблицу
with con:
    con.executemany(sql, data)

# выводим содержимое таблицы с покупками на экран
with con:
    data = con.execute("SELECT * FROM orders")
    for row in data:
        print(row)


app = Flask(__name__)

maintext = ""

@app.route('/')
def hello():
    return render_template('hello.html', x=maintext)


if __name__ == '__main__':
    app.run()
