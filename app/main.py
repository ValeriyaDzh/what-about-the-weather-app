import logging
from fastapi import FastAPI

from .routers import weater_router

# logger setting
logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s : [%(levelname)s] : %(message)s",
)

# FastAPI app

app = FastAPI(title="WATW")

app.include_router(weater_router, prefix="/api")
