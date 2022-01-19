from fastapi.responses import HTMLResponse
from app import app, templates
from fastapi import Request, Depends
from app import validation
from app import fragment
from sqlalchemy.orm import Session
from app.database import get_db


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """Return website home page."""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
async def returning_the_found_passage(phrase_obj: validation.PhraseJSON, db: Session = Depends(get_db)):
    """Function for getting a phrase and return the found passage."""
    phrase = phrase_obj.phrase
    fragment_text = await fragment.return_fragment(phrase, db)
    return {"fragment_text": fragment_text}
