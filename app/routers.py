from fastapi import APIRouter, status, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.exeptions import NotFoundException, UnprocessableEntityException
from app.services import get_weater_today

weater_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@weater_router.get("", status_code=status.HTTP_200_OK)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@weater_router.post(
    "/weater", status_code=status.HTTP_200_OK, response_class=HTMLResponse
)
async def get_weater(request: Request, city: str = Form(...)):
    try:
        data = await get_weater_today(city)
        return templates.TemplateResponse(
            "index.html", {"request": request, "weather": data, "city": city}
        )
    except (NotFoundException, UnprocessableEntityException) as e:
        return templates.TemplateResponse(
            "index.html", {"request": request, "error": e}
        )
