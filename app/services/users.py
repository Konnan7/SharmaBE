import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import Users

from app.clients.db import DatabaseClient


class UserService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_user(self, session: AsyncSession,
                          surname1: str,
                          surname2: str,
                          date_of_birth: datetime.date,
                          email: str,
                          phone_number: str,
                          phone_prefix: int,
                          foot_number: float,
                          pref_club_id: int,
                          account_stripe_id: str = None,
                          reduced: bool = False,
                          end_reduced: datetime.date = None):

        new_user = Users(surname1=surname1,
                         surname2=surname2,
                         date_of_birth=date_of_birth,
                         email=email,
                         phone_number=phone_number,
                         phone_prefix=phone_prefix,
                         foot_number=foot_number,
                         pref_club_id=pref_club_id,
                         account_stripe_id=account_stripe_id,
                         reduced=reduced,
                         end_reduced=end_reduced)
        session.add(new_user)
        await session.commit()
        return new_user

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
