import os
from os.path import join

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from db0mb3r.app.routers import attack, services, index

app = FastAPI(title="db0mb3r")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

app.mount(
    "/static", StaticFiles(directory=join(os.getcwd(), "app", "static")), name="static"
)

app.include_router(attack.router, prefix="/attack", tags=["attack"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(index.router)
