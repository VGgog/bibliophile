from sqlalchemy import Column, Integer, String
from app.admin.database import base


class Urls(base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    author = Column(String)
    book_title = Column(String)
    max_page = Column(Integer)

    def __repr__(self):
        return self.url
