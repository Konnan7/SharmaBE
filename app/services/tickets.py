import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Select

from models.tickets import Tickets
from app.schemas.token import TokenData
from app.schemas.tickets import TicketCreate, TicketResponse

from app.clients.db import DatabaseClient
from app.dependencies import generate_random_string


class TicketService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_ticket(self, phone_number: str, ticket: TicketCreate):
        user_id = await self._get_user_id_by_phone_number(phone_number)
        qr_id = generate_random_string()
        # try:
        new_ticket = Tickets(status=ticket.status, #CHECKPOINT
                             qr_id=qr_id,
                             payment_id=ticket.payment_id, #pendiente actualizar
                             rate_snapshot=ticket.rate_snapshot, #JSON amb la info dels rates
                             user_id=user_id)
        self.database_client.session.add(new_ticket)
        self.database_client.session.commit()
        ticket_response = TicketResponse(ticket_id=new_ticket.ticket_id,
                                         status=new_ticket.status,
                                         date_of_creation=new_ticket.date_of_creation,
                                         qr_id=new_ticket.qr_id,
                                         payment_id=new_ticket.payment_id,
                                         rate_snapshot=new_ticket.rate_snapshot,
                                         user_id=new_ticket.user_id)

        # except:
        # self.database_client.session.rollback()

        return ticket_response

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

    async def _get_user_id_by_phone_number(self, phone_number: str = None) -> Select:
        #consulta que devuelve solo los datos del usuario de la tabla usuario con phone_number
        query = (
            Select(self.database_client.users)
            .where(self.database_client.users.c.phone_number == phone_number)
        )

        user = await self.database_client.get_first(query)
        user_id = user["user_id"]
        return user_id