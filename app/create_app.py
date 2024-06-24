from fastapi import FastAPI

from app.routes.qr import create_router
from app.config import Config

from app.clients.db import DatabaseClient




def create_application() -> FastAPI:
    config = Config()
    tables = ["usuarios", "tarifas"]

    redis_cache = RedisCache(config)
    database_client = DatabaseClient(config)
    router = create_router()


    app = FastAPI()
    app.include_router(router)  # incluye las rutas de qr.py, habra que añadir mas

    return app
