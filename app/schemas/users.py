from datetime import date

from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
from app.schemas.tickets import ListaEntradas



class Tarifa(BaseModel):
    centro: Literal["Gava", "Barcelona", "Madrid"]
    tipo: str


class User(BaseModel):
    Name: str
    Surname1: str
    Surname2: Optional[str]
    Date_of_birth: date  # Puedes usar tipos específicos para fechas si lo prefieres
    # tariff: Optional[Tarifa]  # Relación con la clase Tarifa
    Email: EmailStr
    Phone_prefix: str
    Phone_number: str
    Foot_number: Optional[float]
    # available_tickets: Optional[ListaEntradas]
    Pref_club_id: int
    # user_tickets: Optional[ListaEntradas]
    Account_stripe_id: str
    Reduced: bool
    End_reduced: date
