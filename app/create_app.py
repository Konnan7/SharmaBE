from fastapi import FastAPI

from SharmaBE.app.routes.qr import create_qr_router
from SharmaBE.app.config import Config

from SharmaBE.app.clients.db import DatabaseClient




def create_application() -> FastAPI:
    config = Config()
    tables = ["usuarios", "tarifas"]

    redis_cache = RedisCache(config)
    database_client = DatabaseClient(config)
    qr_router = create_qr_router()


    app = FastAPI()
    app.include_router(router)  # incluye las rutas de qr.py, habra que añadir mas

    return app
