from pydantic import BaseModel
from datetime import datetime


class PaymentBase(BaseModel):
    amount: float
    currency: str = "eur"
    description: str = "Sharma tickets"
    external_payment_id: int


class PaymentCreate(PaymentBase):
    pass


class CreateStripePayment(BaseModel):
    amount: int
    currency: str = "eur"
    description: str = "Sharma Tickets"
    payment_method_types: list[str] = ["card"]

class StripePaymentId(BaseModel):
    id: int
    pass


class Payment(PaymentBase):
    payment_id: int
    date_of_creation: datetime

    class Config:
        orm_mode = True
