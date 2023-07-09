from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import CommentsRepository


app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = CommentsRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/comments")
def get_all_comments(request: Request):
    comments = repository.get_all()
    return templates.TemplateResponse("comments/index.html", {"request": request, "comments": comments})


@app.get("/comments/new")
def get_new_comment(request: Request):
    return templates.TemplateResponse("comments/add_comment.html", {"request": request})


@app.post("/comments/new")
def post_new_comment(comment: str=Form(), category: bool=Form()):
    repository.append({"comment": comment, "category": category})
    return RedirectResponse("/comments", status_code=303)
