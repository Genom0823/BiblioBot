import sqlite3
import requests
from enum import Enum


isbn_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'


class BookData(Enum):
    TITLE = 'title'
    AUTHOR = 'authors'
    DESCRIPTION = 'description'
    IMAGE = 'imageLinks'


def init_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn


def close_database(conn):
    conn.close()


def get_book_info(isbn, data):
    try:
        book = requests.get(f'{isbn_url}{isbn}')
        res = book.json()

        if data == BookData.IMAGE:
            return res["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        
        else:
            return res["items"][0]["volumeInfo"][data.value]
    
    except:
        print('Network Error')
        return None
