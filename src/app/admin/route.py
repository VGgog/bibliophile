from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from .. import app
from ..database import db_crud, get_db
from . import schema
from config import Config


@app.post("/admin/add")
async def add_book_data_in_db(data: schema.Book, db: Session = Depends(get_db)):
    """Function add book data(text-url, author, book_title etc.) in db."""
    if not data.token == Config.admin_token:
        raise HTTPException(status_code=403, detail="You don't have rights")

    if db_crud.check_book_in_db(db=db, book_title=data.book_title):
        raise HTTPException(status_code=400, detail="Book already added")

    return db_crud.add_book_in_db(db=db, data=data)
