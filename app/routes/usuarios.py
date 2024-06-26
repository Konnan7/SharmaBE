import logging

from fastapi import APIRouter
<<<<<<< HEAD
from SharmaBE.app.schemas.usuarios import User
from SharmaBE.app.services.usuarios import UserService
from SharmaBE.app.clients.db import DatabaseClient
=======
from app.schemas.usuarios import User
from app.services.usuarios import UserService
from app.clients.db import DatabaseClient
>>>>>>> ff1a877 (Añadido repositorio de BBDD)



logger = logging.getLogger(__name__)


def create_user_router(database_client:DatabaseClient) -> APIRouter:
    user_router = APIRouter()
    user_service = UserService(database_client)


    @user_router.post("/")
    async def add_user(user_profile: User):
        user = await user_service.create_user(user_profile)
        return user.id


    @user_router.on_event("startup")
    async def startup():
        await database_client.connect()

    @user_router.on_event("shutdown")
    async def shutdown():
        await database_client.disconnect()



    return user_router
