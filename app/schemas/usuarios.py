from typing import Optional
from pydantic import BaseModel, EmailStr


class Tarifa(BaseModel):
    centro: str
    tipo: str


class User(BaseModel):
    nombre: str
    apellido1: str
    apellido2: str
    fecha_nacimiento: str  # Puedes usar tipos específicos para fechas si lo prefieres
    id_usuario: int  # Primary key
    tarifa: Optional[Tarifa]  # Relación con la clase Tarifa
    email: EmailStr
    numero_telefono: int
    numero_pie: float
    entradas_disponibles: int
    club_preferencia: str
