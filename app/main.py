from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    message = """

— Смогла ли я поселиться в твоём сердце?
— Да ты вломилась в него не снимая обуви..

Аракава Наоси "Твоя апрельская ложь"
"""
    return templates.TemplateResponse("home.html", {"request": request, "message": message})


@app.post("/test")
def test_page(message: str = Form(...)):
    message_test = message
    print(message_test)
    return {"message": message_test}

