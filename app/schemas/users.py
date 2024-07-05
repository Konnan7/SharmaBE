from datetime import date

from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
from app.schemas.tickets import ListaEntradas



class Tarifa(BaseModel):
    centro: Literal["Gava", "Barcelona", "Madrid"]
    tipo: str


class User(BaseModel):
    name: str
    surname1: str
    surname2: Optional[str]
    date_of_birth: date  # Puedes usar tipos específicos para fechas si lo prefieres
    # tariff: Optional[Tarifa]  # Relación con la clase Tarifa
    email: EmailStr
    phone_prefix: str
    phone_number: str
    foot_number: Optional[float]
    # available_tickets: Optional[ListaEntradas]
    pref_club_id: int
    # user_tickets: Optional[ListaEntradas]
    account_stripe_id: str
    reduced: bool
    end_reduced: date


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    phone_number: str
    password: str


class TokenData(BaseModel):
    phone_number: str | None = None
