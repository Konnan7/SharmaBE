import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.payments import Payments

from app.clients.db import DatabaseClient


class PaymentService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_payment(self, session: AsyncSession, price: float, tax: float, external_payment_id: int):
        new_payment = Payments(price=price, tax=tax, external_payment_id=external_payment_id)
        session.add(new_payment)
        await session.commit()
        return new_payment

    async def get_payment_by_id(self, session: AsyncSession, payment_id: int):
        payment = await session.execute(select(Payments).filter(Payments.payment_id == payment_id)).scalar()
        return payment

    async def update_payment(self, session: AsyncSession, payment_id: int, **kwargs):
        async with session.begin():
            payment = await session.get(Payments, payment_id)
            if payment:
                for key, value in kwargs.items():
                    setattr(payment, key, value)
        return payment

    async def delete_payment(self, session: AsyncSession, payment_id: int):
        async with session.begin():
            payment = await session.get(Payments, payment_id)
            if payment:
                await session.delete(payment)
        return payment
