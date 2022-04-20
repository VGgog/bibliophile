from sqlalchemy.orm import Session

from .. import models


def check_book_in_db(db: Session, book_title):
    """Check availability of the book(text-url, author, book title etc.) in db"""
    return db.query(models.Book).filter(models.Book.book_title == book_title).first()


def number_of_books(db: Session):
    """Return number of books in db"""
    return db.query(models.Book).count()


def return_book(db: Session, book_id):
    """Return book obj from db"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()
