from sqlalchemy.orm import Session

from app.admin import models
from app.admin import schema


def add_book_in_db(db: Session, data: schema.Book):
    """Add book-data(text-url, author, book title etc.) in db"""
    data_for_add = models.Book(url=data.url, author=data.author,
                               book_title=data.book_title, max_page=data.max_page)
    db.add(data_for_add)
    db.commit()
    db.refresh(data_for_add)
    return data_for_add


def check_book_in_db(db: Session, book_title):
    """Check availability of the book(text-url, author, book title etc.) in db"""
    return db.query(models.Book).filter(models.Book.book_title == book_title).first()
