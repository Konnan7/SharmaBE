import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.tickets import Tickets

from app.clients.db import DatabaseClient


class TicketService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_ticket(self, session: AsyncSession,
                            status: str,
                            qr_id: str,
                            payment_id: int,
                            rate_snapshot=None):
        new_ticket = Tickets(status=status,
                             qr_id=qr_id,
                             payment_id=payment_id,
                             rate_snapshot=rate_snapshot)
        session.add(new_ticket)
        await session.commit()
        return new_ticket

    async def get_ticket_by_id(self, session: AsyncSession, ticket_id: int):
        ticket = await session.execute(select(Tickets).filter(Tickets.ticket_id == ticket_id)).scalar()
        return ticket

    async def update_ticket(self, session: AsyncSession, ticket_id: int, **kwargs):
        async with session.begin():
            ticket = await session.get(Tickets, ticket_id)
            if ticket:
                for key, value in kwargs.items():
                    setattr(ticket, key, value)
        return ticket

    async def delete_ticket(self, session: AsyncSession, ticket_id: int):
        async with session.begin():
            ticket = await session.get(Tickets, ticket_id)
            if ticket:
                await session.delete(ticket)
        return ticket
