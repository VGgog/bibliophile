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


def create_new_row_with_book(db: Session, book):
    """"""
    db.add(models.Book(author=book.author,
                       book_title=book.title,
                       text=book.text))
    return db.commit()
