from fastapi import FastAPI


from app.routes.qr import create_qr_router
from app.routes.usuarios import create_user_router
from app.config import Config

from app.clients.db import DatabaseClient



def create_application() -> FastAPI:
    config = Config()
    tables = ["usuarios"]

    database_client = DatabaseClient(config,tables)
    qr_router = create_qr_router(database_client)
    user_router = create_user_router(database_client)

    app = FastAPI()
    app.include_router(qr_router)  # incluye las rutas de qr.py, habra que añadir mas
    app.include_router(user_router)
    return app
