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

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    status: Optional[str] = None

class Ticket(TicketBase):
    ticket_id: int
    date_of_creation: datetime
    user_id: Optional[int] = None

    class Config:
        orm_mode = True




