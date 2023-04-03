import sqlite3
import requests


isbn_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

def init_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn


def close_database(conn):
    conn.close()


def get_book_info(isbn):
    try:
        book = requests.get(f'{isbn_url}{isbn}')
        res = book.json()
        return res
    
    except:
        print('Network Error')
        return None
