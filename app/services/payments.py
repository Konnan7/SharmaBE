import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.payments import Payments

from app.schemas.payments import PaymentCreate

from app.clients.db import DatabaseClient


class PaymentService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client
        self.session = self.database_client.session

    async def create_payment(self, payment: PaymentCreate):
        new_payment = Payments(amount=payment.amount, currency=payment.currency, external_payment_id=payment.external_payment_id)
        self.session.add(new_payment)
        await self.session.commit()
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


