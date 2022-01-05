from fastapi.responses import HTMLResponse
from app import app, templates
from fastapi import Request
from app import validation


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    """Return website home page."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
def returning_the_found_passage(phrase_obj: validation.PhraseJSON):
    """Function for getting a phrase and return the found passage."""
    fragment_text = phrase_obj.phrase
    return {"fragment_text": fragment_text}
