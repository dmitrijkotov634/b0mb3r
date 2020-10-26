import os
from os.path import join

from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from loguru import logger

from db0mb3r.service import prepare_services

router = APIRouter()
templates = Jinja2Templates(directory=join(os.getcwd(), "app", "templates"))


@logger.catch
@router.get("/")
def index(request: Request):
    if request.app.state.only_api:
        raise HTTPException(status_code=404)

    services = prepare_services()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "service_count": len(services[7]),
        },  # 7 corresponds to Russia which is a default choice
    )
