from sqlalchemy.orm import Session
from app.admin import models
from app.admin import schema


def add_url(db: Session, url_data: schema.URLModel):
    data = models.Urls(url=url_data.url, author=url_data.author, 
            book_tile=url_data.book_title, max_page=url_data.max_page)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
