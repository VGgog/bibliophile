from sqlalchemy.orm import Session

from ..scheme import AddBookValidation
from src.app.database import db_crud


class AdminService:

    def add_book(
        self, 
        db: Session,
        book_data: AddBookValidation
    ) -> bool:
        """
        Method which add new book in db.
        Return False if the book is in the database.
        Return True if the book not in database
        """
        if db_crud.check_book_in_db(db=db, book_title=book_data.title):
            return False

        return True
