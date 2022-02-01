from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.admin import models
from app.database import base, engine


app = FastAPI()
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

models.base.metadata.create_all(bind=engine)

from app import routes
from app.admin import route
