from fastapi import FastAPI

from .routers import weater_router

app = FastAPI(title="WATW")

app.include_router(weater_router, prefix="/api")
