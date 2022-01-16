from sqlalchemy.orm import Session
from app.admin import models
from app.admin import schema


def add_url(db: Session, url_data: schema.Book):
    data = models.Book(url=url_data.url, author=url_data.author,
                       book_title=url_data.book_title, max_page=url_data.max_page)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def check_url_in_db(db: Session, url):
    return db.query(models.Book).filter(models.Book.url == url).first()
