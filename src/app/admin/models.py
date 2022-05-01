from sqlalchemy import Column, Integer, String

from ..database import base


class Book(base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    author = Column(String)
    book_title = Column(String)
    max_page = Column(Integer)
