from typing import Optional, Literal
from pydantic import BaseModel, EmailStr


from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketBase(BaseModel):
    status: str
    qr_id: str
    payment_id: int
    rate_snapshot: str


class TicketResponse(BaseModel):
    ticket_id: int
    status: str
    date_of_creation: datetime
    qr_id: str
    payment_id: int
    rate_snapshot: str
    user_id: int

class TicketCreate(BaseModel):
    rate_snapshot: str
    status: str = "Available"
    payment_id: int = 1

class TicketUpdate(BaseModel):
    status: Optional[str] = None

class Ticket(BaseModel):
    ticket_id: int
    date_of_creation: datetime
    user_id: Optional[int] = None

class TicketList(BaseModel):
    list_of_tickets: list[Ticket]
    class Config:
        orm_mode = True




