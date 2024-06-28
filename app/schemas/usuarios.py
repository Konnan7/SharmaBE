from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
from app.schemas.entradas import ListaEntradas



class Tarifa(BaseModel):
    centro: Literal["Gava", "Barcelona", "Madrid"]
    tipo: str


class User(BaseModel):
    name: str
    surname1: str
    surname2: str
    date_of_birth: str  # Puedes usar tipos específicos para fechas si lo prefieres
    user_id: int  # Primary key
    # tariff: Optional[Tarifa]  # Relación con la clase Tarifa
    email: EmailStr
    phone_prefix: int
    phone_number: int
    foot_number: float
    available_tickets: ListaEntradas
    pref_club: int
    tickets: ListaEntradas
