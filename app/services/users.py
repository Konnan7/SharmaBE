import datetime
from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from models.users import Users
from app.schemas.users import User
import app.exceptions as exceptions

from app.clients.db import DatabaseClient


class UserService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client


    async def create_user(self,
                          user: User):
        #try:
            new_user = Users(Name=user.Name,
                             Surname1=user.Surname1,
                             Surname2=user.Surname2,
                             Date_of_birth=user.Date_of_birth,
                             Email=user.Email,
                             Phone_number=user.Phone_number,
                             Phone_prefix=user.Phone_prefix,
                             Foot_number=user.Foot_number,
                             Pref_club_id=user.Pref_club_id,
                             Account_stripe_id=user.Account_stripe_id,
                             Reduced=user.Reduced,
                             End_reduced=user.End_reduced)
            self.database_client.session.add(new_user)
            self.database_client.session.commit()
            res = new_user.user_id
            return res
        #except IntegrityError as e:
        #    self.database_client.session.rollback()
        #    raise exceptions.UserAlreadyExists


    async def get_user_by_id(self,  user_id: int = 0) -> User:
        query = self._get_user_info_query(user_id)
        user = await self.database_client.get_first(query)
        user_info = dict(zip(user._mapping.keys(), user._mapping.values()))

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