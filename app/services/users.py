import datetime
from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from models.users import Users
from app.schemas.users import User
from app.services.auth import AuthService
from app.exception_handlers import UserNotFound, UserAlreadyExists

from app.clients.db import DatabaseClient

import logging
logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client


    async def create_user(self,
                          user: User,
                          password: str) -> int:
        db_user = self.database_client.session.query(Users).filter(Users.phone_number == user.phone_number).first()
        logging.debug(f"db_user query is: {db_user}")

        #Miro si ya existe el user que intentamos crear
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")

        hashed_password = AuthService.get_password_hash(password)

        try:
            new_user = Users(name=user.name,
                             surname1=user.surname1,
                             surname2=user.surname2,
                             date_of_birth=user.date_of_birth,
                             email=user.email,
                             phone_number=user.phone_number,
                             phone_prefix=user.phone_prefix,
                             foot_number=user.foot_number,
                             pref_club_id=user.pref_club_id,
                             account_stripe_id=user.account_stripe_id,
                             reduced=user.reduced,
                             end_reduced=user.end_reduced,
                             hashed_password=hashed_password)
            self.database_client.session.add(new_user)
            self.database_client.session.commit()
            res = new_user
        except:
            self.database_client.session.rollback()
            raise UserAlreadyExists
        return res.user_id

    async def get_user_by_id(self,  user_id: int = 0) -> User:
        query = self._get_user_info_query(user_id)
        user = await self.database_client.get_first(query)
        if user:
            user_info = dict(zip(user._mapping.keys(), user._mapping.values()))
        else:
            raise UserNotFound(user_id)
        return User(**user_info)

    async def update_user(self, session: AsyncSession, user_id: int, **kwargs):
        async with session.begin():
            user = await session.get(Users, user_id)
            if user:
                for key, value in kwargs.items():
                    setattr(user, key, value)
        return user

    async def delete_user(self, session: AsyncSession, user_id: int):
        async with session.begin():
            user = await session.get(Users, user_id)
            if user:
                await session.delete(user)
        return user


    def _get_user_info_query(self, user_id: Optional[int] = None) -> Select:
        #consulta que devuelve solo los datos del usuario de la tabla usuario con id:user_id
        query = (
            Select(self.database_client.users)
                 .where(self.database_client.users.c.user_id == user_id)
        )
        return query