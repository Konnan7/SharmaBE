from fastapi import FastAPI, APIRouter
import uvicorn

from routes.qr import create_router


def create_application() -> FastAPI:

    router = create_router()

    app = FastAPI()
    app.include_router(router)

    return app
