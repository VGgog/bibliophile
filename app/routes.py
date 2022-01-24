import random

from fastapi.responses import HTMLResponse
import aiohttp
from fastapi import Request

from app import app, templates
from app import validation
from app import fragment
from app.database import session, db_crud


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """Return website home page."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
async def returning_the_found_passage(phrase_obj: validation.PhraseJSON):
    """Function for getting a phrase and return the found passage."""
    phrase = phrase_obj.phrase
    result = await searching(phrase)
    return {"fragment_text": result}


async def searching(phrase):
    """Searching fragment."""
    fragment_text = None
    step = 0
    async with aiohttp.ClientSession() as cl_session:
        while not fragment_text and step < 25:
            try:
                db = session()
                book = db_crud.return_book(db, random.randrange(1, db_crud.number_of_books(db)+1))

                if book.max_page != 1:
                    url = book.url[:-11] + "/p." + str(random.randrange(1, book.max_page + 1)) + book.url[-11:]
                else:
                    url = book.url[:-11] + "/p.1" + book.url[-11:]

                async with cl_session.get(url) as response:
                    html_text = await response.text()
                    book = fragment.GetFragment(phrase, db, html_text)

            finally:
                db.close()
            fragment_text = book.result
            step += 1

        if fragment_text:
            return fragment_text
        else:
            return "Отрывок не найден..."
