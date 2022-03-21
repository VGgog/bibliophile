import re
import random

from bs4 import BeautifulSoup

from app.database import db_crud


def get_book(db):
    """Get random book in db"""
    return db_crud.return_book(db=db, book_id=random.randrange(1, db_crud.number_of_books(db)+1))


def get_text_link(book):
    """
    Return text_link.
    example: book_url = https://ilibrary.ru/text/11/index.html
    But text located at the link https://ilibrary.ru/text/11/p.{number of page}/index.html.
    Due to this function converts book_url to the text_link when text located.
    Number of page = random number before max_page
    book.url[:-11] = https://ilibrary.ru/text/11
    book.url[-11:] = /index.html
    """
    if book.max_page != 1:
        return book.url[:-11] + "/p." + str(random.randrange(1, book.max_page + 1)) + book.url[-11:]
    else:
        return book.url[:-11] + "/p.1" + book.url[-11:]


def get_text(html_text):
    """Return text of the book"""
    pars_obj = BeautifulSoup(html_text, 'lxml')
    text = pars_obj.find('div', id='text')
    return text.text


def search_fragment_in_text(phrase, text):
    """
    Search need phrase in text.
    If fragment was found return fragment.
    Else return None.
    """
    paragraph_after_phrase = ".*\n"
    paragraph_before_phrase = "\n.*"
    result = re.search(paragraph_before_phrase + phrase + paragraph_after_phrase, text)
    if result:
        fragment = result[0].strip()

        while fragment[-1] not in ['.', '?', '!', '»']:
            paragraph_after_phrase += ".*\n"
            result = re.search(paragraph_before_phrase + phrase + paragraph_after_phrase, text)
            if not result:
                return None
            fragment = result[0].strip()

        while ('»' in fragment) and ('«' not in fragment):
            paragraph_before_phrase += "\n.*"
            result = re.search(paragraph_before_phrase + phrase + paragraph_after_phrase, text)
            if not result:
                return None
            fragment = result[0].strip()

        return fragment

    return None
