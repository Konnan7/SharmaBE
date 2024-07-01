from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.rates import Rates

from app.clients.db import DatabaseClient


class RateService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_rate(self, session: AsyncSession, price: int, type: str, club_id: int):
        new_rate = Rates(price=price, type=type, club_id=club_id)
        session.add(new_rate)
        await session.commit()
        return new_rate

    async def get_rate_by_id(self, session: AsyncSession, rate_id: int):
        rate = await session.execute(select(Rates).filter(Rates.rate_id == rate_id)).scalar()
        return rate

    async def update_rate(self, session: AsyncSession, rate_id: int, **kwargs):
        async with session.begin():
            rate = await session.get(Rates, rate_id)
            if rate:
                for key, value in kwargs.items():
                    setattr(rate, key, value)
        return rate

    async def delete_rate(self, session: AsyncSession, rate_id: int):
        async with session.begin():
            rate = await session.get(Rates, rate_id)
            if rate:
                await session.delete(rate)
        return rate
