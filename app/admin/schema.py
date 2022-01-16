from pydantic import BaseModel


class URLModel(BaseModel):
    """Model request on add book-url"""
    token: str
    url: str
    author: str
    book_title: str
    max_page: int

    class Config:
        orm_mode = True

