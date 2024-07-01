from datetime import date

from typing import Optional, Literal
from pydantic import BaseModel, EmailStr



class Club(BaseModel):
    Club_id = int
    Horarios = str
    Location = str
    Name = str
    Status = str