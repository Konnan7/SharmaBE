from fastapi import FastAPI, APIRouter
import uvicorn
import os

from app.routes.qr import create_router


def create_application() -> FastAPI:

    router = create_router()

    app = FastAPI()
    app.include_router(router)

    return app
