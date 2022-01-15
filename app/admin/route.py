from app import app
from app.admin import db_crud
from app.admin import models
from app.admin import schema
from app.admin.database import engine, session


models.base.metadata.create_all(bind=engine)

