from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
<<<<<<< HEAD
from SharmaBE.app.schemas.entradas import ListaEntradas
=======
from app.schemas.entradas import ListaEntradas
>>>>>>> ff1a877 (Añadido repositorio de BBDD)


class Tarifa(BaseModel):
    centro: Literal["Gava", "Barcelona", "Madrid"]
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
    entradas: ListaEntradas
