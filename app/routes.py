from fastapi.responses import HTMLResponse
from fastapi import Request

from app import app, templates
from app import validation
from app.result import get_result


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """Return website home page."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
async def returning_the_found_passage(phrase_obj: validation.PhraseJSON):
    """Function for getting a phrase and return the found passage."""
    phrase = phrase_obj.phrase
    fragment = await get_result(phrase)
    return {"fragment_text": fragment}
