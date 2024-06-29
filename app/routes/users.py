import logging

from fastapi import APIRouter
from models.users import Users
from app.services.users import UserService
from app.clients.db import DatabaseClient




logger = logging.getLogger(__name__)


def create_user_router(database_client:DatabaseClient) -> APIRouter:
    user_router = APIRouter()
    user_service = UserService(database_client)


    @user_router.post("/")
    async def add_user(user_profile: Users):
        user = await user_service.create_user(user_profile)
        return user.id


    @user_router.on_event("startup")
    async def startup():
        await database_client.connect()

    @user_router.on_event("shutdown")
    async def shutdown():
        await database_client.disconnect()



    return user_router
