from fastapi import FastAPI

from app.exception_handlers import add_exception_handlers

from app.routes.qr import create_qr_router
from app.routes.users import create_user_router
from app.routes.tickets import create_ticket_router

from app.config import Config

from app.clients.db import DatabaseClient



def create_application() -> FastAPI:
    config = Config()
    tables = ["users", "tickets", "clubs", "rates", "payments"]

    database_client = DatabaseClient(config,tables)
    qr_router = create_qr_router(database_client)
    user_router = create_user_router(database_client)
    ticket_router = create_ticket_router(database_client)

    app = FastAPI()
#Routers
    app.include_router(qr_router)  # incluye las rutas de qr.py, habra que añadir mas
    app.include_router(user_router)
    app.include_router(ticket_router)
    add_exception_handlers(app)
    return app
