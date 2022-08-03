from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from db.tables import User
from services.users import current_active_user

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")



@router.get("/p/auth", response_class=HTMLResponse)
async def page(request: Request, user: User = Depends(current_active_user)):
    return templates.TemplateResponse("hi.html", {"request": request, "user": user.email})

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("hi.html", {"request": request, "data": data})

@router.get("/page/{page_name}", response_class=HTMLResponse)
async def page(page_name: str, request: Request):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@router.get("/test", response_class=HTMLResponse)
def form_post1(request: Request):
    return templates.TemplateResponse('test.html', {'request': request})

@router.get("/test1", response_class=HTMLResponse)
def form_post1(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})