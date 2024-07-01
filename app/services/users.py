import datetime
from sqlalchemy import select
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
            new_user = Users(Name=user.name,
                             Surname1=user.surname1,
                             Surname2=user.surname2,
                             Date_of_birth=user.date_of_birth,
                             Email=user.email,
                             Phone_number=user.phone_number,
                             Phone_prefix=user.phone_prefix,
                             Foot_number=user.foot_number,
                             Pref_club_id=user.pref_club_id,
                             Account_stripe_id=user.account_stripe_id,
                             Reduced=user.reduced,
                             End_reduced=user.end_reduced)
            self.database_client.session.add(new_user)
            self.database_client.session.commit()
            res = new_user.user_id
            return res
        #except IntegrityError as e:
        #    self.database_client.session.rollback()
        #    raise exceptions.UserAlreadyExists


    async def get_user_by_id(self, session: AsyncSession, user_id: int):
        user = await session.execute(select(Users).filter(Users.user_id == user_id)).scalar()
        return user

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
