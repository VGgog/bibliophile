from pydantic import BaseModel


class URLModel(BaseModel):
    url: str
    author: str
    book_title: str
    max_page: int

    class Config:
        orm_mode = True

