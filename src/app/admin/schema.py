from pydantic import BaseModel


class Book(BaseModel):
    """Model validate admin-request on add book in db"""
    token: str
    url: str
    author: str
    book_title: str
    max_page: int

    class Config:
        orm_mode = True
