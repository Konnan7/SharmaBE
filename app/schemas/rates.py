from typing import Optional, Literal
from pydantic import BaseModel, EmailStr


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Rates(BaseModel):
    rate_id: int
    amount: int = Field()
    club_id: int = 1
    type: str


class StripeRates(BaseModel):
    amount: int  # Debe ponerse en centavos y *100
    currency: str  # eur
    payment_method_types: list[str]  # ['card']


class RateList(Rates):
    list_of_rates: list[Rates]

