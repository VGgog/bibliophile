from pydantic import BaseModel


class BookScheme(BaseModel):
    """Book validation"""
    author: str
    title: str
    text: str


class AddBookValidation(BookScheme):
    """Book addition validation"""
    token: str
