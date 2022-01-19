import re
import random

import requests
from bs4 import BeautifulSoup

from app.database import db_crud


def get_book(db):
    """Get book in db"""
    book_id = random.randrange(1, db_crud.number_of_books(db)+1)
    return db_crud.return_book(db=db, book_id=book_id)
   

def get_book_url(book):
    """Return book url"""    
    if book.max_page != 1:
        return book.url[:-11] + "/p." + str(random.randrange(1, book.max_page + 1)) + book.url[-11:]
    else:
        return book.url[:-11] + "/p.1"  + book.url[-11:]


def make_request(url):
    """Makes request on book url, and return html_text"""
    response = requests.get(url)
    return response.text


def get_text(html_text):
    """Return text of the book"""
    pars_obj = BeautifulSoup(html_text, 'lxml')
    text =  pars_obj.find('div', id='text')
    return text.text


def search_fragment(phrase, text):
    """Search need phrase in text and return fragmnet"""
    result = re.search("\n.*"+phrase+".*\n", text)
    if result:
        fragment = result[0].strip()
        # If fragment close ":"(in russian language most often it means that text ends with a direct speech), that take next paragraph
        if fragment[-1] == ":":
            new_fragment = re.search("\n.*"+phrase+".*\n.*\n", text)
            return new_fragment[0].strip()
        else:
            return fragment

    return None



async def return_fragment(phrase, db):
    """return fragment from text"""
    book = get_book(db)
    url = get_book_url(book)
    text = get_text(make_request(url)) 
    result = search_fragment(phrase, text)
    if result:
        return result
    else:
        return "Отрывок не удалось найти..."

