from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/templates/html")

@router.get("/sing-in", response_class=HTMLResponse)
def form_post1(request: Request):
    return templates.TemplateResponse('sing-in.html', {'request': request})

@router.get("/sing-up", response_class=HTMLResponse)
def form_post1(request: Request):
    return templates.TemplateResponse('sing-up.html', {'request': request})

@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, remail: str = Form(), pwd: str = Form()):
    data = {
        'email': remail,
        'pwd': pwd
    }
    return templates.TemplateResponse('sing-in.html', {'request': request, 'data': data})