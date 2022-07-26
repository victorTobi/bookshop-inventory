import sqlite3






def connect():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('')