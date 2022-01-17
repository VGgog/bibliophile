from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app import app
from app.database import db_crud
from app.admin import models
from app.admin import schema
from app.database import engine, session
from config import Config


models.base.metadata.create_all(bind=engine)


def get_db():
    """Create dependency"""
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post("/admin/add")
async def add_book_data_in_db(data: schema.Book, db: Session = Depends(get_db)):
    """Function add book data(text-url, author, book_title etc.) in db."""
    if not data.token == Config.admin_token:
        raise HTTPException(status_code=403, detail="You don't have rights")

    if db_crud.check_book_in_db(db=db, book_title=data.book_title):
        raise HTTPException(status_code=400, detail="Book already added")
    
    return db_crud.add_book_in_db(db=db, data=data)
