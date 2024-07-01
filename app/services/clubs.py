from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.clubs import Clubs

from app.clients.db import DatabaseClient


class ClubService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_club(self, session: AsyncSession, name: str, location: str, status: str, horarios: str = None):
        new_club = Clubs(name=name, location=location, status=status, horarios=horarios)
        session.add(new_club)
        await session.commit()
        return new_club

    async def get_club_by_id(self, session: AsyncSession, club_id: int):
        club = await session.execute(select(Clubs).filter(Clubs.club_id == club_id)).scalar()
        return club

    async def update_club(self, session: AsyncSession, club_id: int, **kwargs):
        async with session.begin():
            club = await session.get(Clubs, club_id)
            if club:
                for key, value in kwargs.items():
                    setattr(club, key, value)
        return club

    async def delete_club(self, session: AsyncSession, club_id: int):
        async with session.begin():
            club = await session.get(Clubs, club_id)
            if club:
                await session.delete(club)
        return club
