import re
import random

import requests
from bs4 import BeautifulSoup

from app.database import db_crud, session


class GetFragment:

    def __init__(self, phrase):

        self.db = session()

        self.phrase = phrase
        self.book_id = random.randrange(1, db_crud.number_of_books(self.db)+1)
        self.book = self.get_book()
        self.text_link = self.get_text_link()
        self.text = self.get_text(self.get_html_text()) 
        self.result = self.search_fragment_in_text()

        self.author = self.book.author
        self.book_title = self.book.book_title

    def get_book(self):
        """Get random book in db"""
        return db_crud.return_book(db=self.db, book_id=self.book_id)
   
    def get_text_link(self):
        """
        Return text_link.
        example: book_url = https://ilibrary.ru/text/11/index.html
        But text located at the link https://ilibrary.ru/text/11/p.{number of page}/index.html. 
        Due to this function converts book_url to the text_link when text located.
        Number of page = random number before max_page 
        book.url[:-11] = https://ilibrary.ru/text/11
        book.url[-11:] = /index.html
        """    
        if self.book.max_page != 1:
            return self.book.url[:-11] + "/p." + str(random.randrange(1, self.book.max_page + 1)) + self.book.url[-11:]
        else:
            return self.book.url[:-11] + "/p.1" + self.book.url[-11:]

    def get_html_text(self):
        """Makes request on text_link, and return html_text"""
        response = requests.get(self.text_link)
        return response.text

    def get_text(self, html_text):
        """Return text of the book"""
        pars_obj = BeautifulSoup(html_text, 'lxml')
        self.text = pars_obj.find('div', id='text')
        return self.text.text
 
    def search_fragment_in_text(self):
        """
        Search need phrase in text.
        If fragment was found return fragment.
        Else return None.
        """
        result = re.search("\n.*"+self.phrase+".*\n", self.text)
        if result:
            fragment = result[0].strip()
            # If fragment close ":"(in russian language most often it means that text ends with a direct speech),
            # that take next paragraph
            if fragment[-1] == ":":
                fragment = re.search("\n.*"+self.phrase+".*\n.*\n", self.text)
                fragment = fragment[0].strip()
                return fragment
            else:
                return fragment
            
        return None
