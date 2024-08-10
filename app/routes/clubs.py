import logging

from fastapi import APIRouter
from models.clubs import Clubs
from app.services.clubs import ClubService
from app.clients.db import DatabaseClient
from app.schemas.clubs import Club


from typing import Optional

logger = logging.getLogger(__name__)


def create_club_router(database_client: DatabaseClient) -> APIRouter:
    club_router = APIRouter()
    club_service = ClubService(database_client)

    @club_router.post("/", status_code=201)
    async def add_user(user_profile: User):
        user_id = await user_service.create_user(user_profile)
        return user_id

    @club_router.get("/{user_id}")
    async def get_user(user_id: Optional[int]) -> User:
        user = await user_service.get_user_by_id(user_id)
        return user


    @club_router.on_event("startup")
    async def startup():
        await database_client.connect()


    @club_router.on_event("shutdown")
    async def shutdown():
        await database_client.disconnect()

    return club_router
