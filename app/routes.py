from fastapi.responses import HTMLResponse
from app import app, templates
from fastapi import Request, Depends
from app import validation
from app import fragment
from sqlalchemy.orm import Session

from app.database import get_db, session


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """Return website home page."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
async def returning_the_found_passage(phrase_obj: validation.PhraseJSON):
    """Function for getting a phrase and return the found passage."""
    phrase = phrase_obj.phrase
    result = searching(phrase)
    return {"fragment_text": result}


def searching(phrase):
    """Searching fragment."""
    fragment_text = None
    step = 0
    while not fragment_text and step < 25:
        book = fragment.GetFragment(phrase)
        fragment_text = book.result
        step += 1

    if fragment_text:
        return fragment_text
    else:
        return "Отрывок не найден..."

