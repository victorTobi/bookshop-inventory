import sqlite3






def connect():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, book_number integer)')
    conn.commit()
    conn.close()


def insert(title, author,year,book_number):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,book_number))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title,author,year,book_number):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR book_number=?")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
insert()