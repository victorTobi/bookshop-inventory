import sqlite3
from turtle import title






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
    conn.close()
    return rows

def search(title="",author="",year="",book_number=""):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR book_number=?", (title,author,year,book_number))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE  id=?", (id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,book_number):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, book_number=? WHERE id=?", (title,author,year,book_number,id))
    conn.commit()
    conn.close()

connect()
#insert("test subject", "john doe", 1657, 34566633)
#update(3, title="liberation", year=2022, author='james', book_number=2299991)
#delete(2)
#print(view())
#print(search(author="Victor Tobi"))