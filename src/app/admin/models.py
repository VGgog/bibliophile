from sqlalchemy import Column, Integer, String

from ..database import base


class Book(base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    author = Column(String)
    book_title = Column(String)
    url = Column(String)
    max_page = Column(Integer)
