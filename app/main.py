from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class PhraseJSON(BaseModel):
    phrase: str


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    """Return website home page."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
def returning_the_found_passage(phrase_obj: PhraseJSON):
    """Function for getting a phrase and return the found passage."""
    fragment_text = phrase_obj.phrase
    return {"fragment_text": fragment_text}
