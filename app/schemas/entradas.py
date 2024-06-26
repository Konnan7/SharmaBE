from typing import Optional, Literal
from pydantic import BaseModel, EmailStr


class Entrada(BaseModel):
    tipo: Literal["Manana", "Dia", "Noche"]
    estado: Literal["Activada", "Desactivada", "Utilizada"]


class ListaEntradas(BaseModel):
    lista: list[Entrada]
    total: int



