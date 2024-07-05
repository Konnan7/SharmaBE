import logging

from app.exception_handlers import UserNotFound
from fastapi import APIRouter
from models.users import Users
from app.services.users import UserService
from app.clients.db import DatabaseClient
from app.schemas.users import User, Token, UserCreate


from typing import Optional

logger = logging.getLogger(__name__)


def create_user_router(database_client: DatabaseClient) -> APIRouter:
    user_router = APIRouter()
    user_service = UserService(database_client)

    @user_router.post("/register", status_code=201)
    async def add_user(user_profile: User, password:str):
        user_id = await user_service.create_user(user_profile, password)
        return user_id

    @user_router.post("/login", response_model=Token)
    def login(user: UserCreate):
        token = user_service.login_for_access_token(user)
        return token

    @user_router.get("/{user_id}")
    async def get_user(user_id: Optional[int]) -> User:
        user = await user_service.get_user_by_id(user_id)
        return user

    @user_router.get("/{token}")
    async def get_user_with_token(token: str) -> User:
        user = await user_service.get_current_user(token)
        return user




    @user_router.on_event("startup")
    async def startup():
        await database_client.connect()

    @user_router.on_event("shutdown")
    async def shutdown():
        await database_client.disconnect()

    return user_router
