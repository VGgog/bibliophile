import multiprocessing

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
    print(phrase)
    with multiprocessing.Pool(2) as pool:
        result = pool.map(searching, (phrase, phrase, phrase))

    return {"fragment_text": result[1]}


def searching(phrase):
    """Searching fragment."""
    db = session()
    fragment_text = None

    while not fragment_text:
        fragment_text = fragment.return_result_of_searching(phrase, db)

    return fragment_text

