from fastapi import APIRouter, HTTPException

from app.clients.db import DatabaseClient

from app.services.auth import AuthService

from app.schemas.users import User
from app.schemas.auth import UserCreate, Token

import logging

logger = logging.getLogger(__name__)


def create_auth_router(database_client: DatabaseClient) -> APIRouter:
   auth_router = APIRouter()
   auth_service = AuthService(database_client)




   # @auth_router.post("/login", response_model=Token)
   # def login(user: UserCreate, db: auth_service.database_client.session = Depends(get_db)):


   return auth_router