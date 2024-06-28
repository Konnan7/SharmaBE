from typing import Optional, Literal
from pydantic import BaseModel, EmailStr


class Entrada(BaseModel):
    tipo: Literal["Manana", "Dia", "Socio"]
    estado: Literal["Activada", "Desactivada", "Utilizada"]
    created_at:


class ListaEntradas(BaseModel):
    lista: list[Entrada]
    total: int



