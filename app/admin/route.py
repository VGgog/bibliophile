from app import app
from app.admin import db_crud
from app.admin import models
from app.admin import schema
from app.admin.database import engine, session
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


models.base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post("/admin/add")
def add_url_in_db(url_data: schema.URLModel, db: Session = Depends(get_db)):
    if db_crud.check_url_in_db(db=db, url=url_data.url):
        raise HTTPException(status_code=400, detail="URL already added")
    return db_crud.add_url(db=db, url_data=url_data)

