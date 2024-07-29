import random
import string
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


from app.schemas.users import TokenData
from app.schemas.rates import Rates

import logging
logger = logging.getLogger(__name__)

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def generate_random_string(length=25):
    # Define los caracteres que se utilizarán para generar la cadena
    characters = string.ascii_letters + string.digits + string.punctuation
    # Genera la cadena aleatoria
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        logging.debug(f"Trying payload")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logging.debug(f"Decode payload: {payload}")

        phone_number: str = payload.get("sub")
        if phone_number is None:
            raise credentials_exception
        token_data = TokenData(phone_number=phone_number)
    except JWTError:
        logging.debug(f"Error verifying credentials")

        raise credentials_exception
    return token_data


def calculate_total_cost(list_of_rates: list[Rates]) -> int:
    total_cost = 0
    for rate in list_of_rates:
        total_cost += rate.amount
    return total_cost
