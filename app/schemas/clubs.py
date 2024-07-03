from datetime import date

from typing import Optional, Literal
from pydantic import BaseModel, EmailStr



class Club(BaseModel):
    club_id = int
    horarios = str
    location = str
    name = str
    status = str