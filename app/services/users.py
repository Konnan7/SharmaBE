from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, status

# Security imports
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt


# App imports
from models.users import Users
from app.schemas.users import User, UserCreate, TokenData, Token, UserUpdate
from app.exception_handlers import UserNotFound, UserAlreadyExists

from app.clients.db import DatabaseClient

import logging
logger = logging.getLogger(__name__)

# Variables de entorno de seguridad
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

    async def create_user(self,
                          user: User,
                          password: str) -> int:
        db_user = self.database_client.session.query(Users).filter(Users.phone_number == user.phone_number).first()
        logging.debug(f"db_user query is: {db_user}")

        #Miro si ya existe el user que intentamos crear
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")

        hashed_password = self.get_password_hash(password)

        try:
            new_user = Users(name=user.name,
                             surname1=user.surname1,
                             surname2=user.surname2,
                             date_of_birth=user.date_of_birth,
                             email=user.email,
                             phone_number=user.phone_number,
                             phone_prefix=user.phone_prefix,
                             foot_number=user.foot_number,
                             pref_club_id=user.pref_club_id,
                             account_stripe_id=user.account_stripe_id,
                             reduced=user.reduced,
                             end_reduced=user.end_reduced,
                             hashed_password=hashed_password)
            logging.debug(f"db_user query is: {new_user}")

            self.database_client.session.add(new_user)
            self.database_client.session.commit()

            res = new_user
        except:
            self.database_client.session.rollback()
            raise UserAlreadyExists
        return res.user_id



    async def get_user_by_id(self,  user_id: int = 0) -> User:
        query = self._get_user_by_user_id_query(user_id)
        user = await self.database_client.get_first(query)
        if user:
            user_info = dict(zip(user._mapping.keys(), user._mapping.values()))
        else:
            raise UserNotFound(user_id)
        return User(**user_info)

    async def get_user_by_phone_number(self,  phone_number: str) -> User:
        query = self._get_user_by_phone_number_query(phone_number)
        user = await self.database_client.get_first(query)
        if user:
            user_info = dict(zip(user._mapping.keys(), user._mapping.values()))
        else:
            raise UserNotFound(phone_number)
        return User(**user_info)

    async def update_user(self, phone_number: str, user_updated:UserUpdate):
        # async with self.database_client.session.begin():
        query = select(Users).where(Users.phone_number == phone_number)
        result = self.database_client.session.execute(query)
        user_info = result.scalar_one_or_none()
        logging.debug(f"User_info is: {user_info}")
        logging.debug(f"User_updated in dictionary format is: {user_updated.dict()}")


        if user_info:
            user_updated_info=user_updated.dict(exclude_none=True)
            for key, value in user_updated_info.items():
                if value is not None:
                    logging.debug(f"For key: {key}, we assigned the value: {value}")
                    setattr(user_info, key, value)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        # user = User(**user_info)
        self.database_client.session.commit()

        return user_info

    async def delete_user(self, phone_number: str):
        async with self.database_client.session.begin():
            user = self._get_user_by_phone_number_query(phone_number)
            if user:
                await self.database_client.session.delete(user)
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
        return print(f"User {phone_number} deleted successfully")

    async def get_current_user(self, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = await self.get_user_by_id(token_data.phone_number)
        if user is None:
            raise credentials_exception
        return user

    def login_for_access_token(self, user: UserCreate):
        db_user = self.database_client.session.query(Users).filter(Users.phone_number == user.phone_number).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        if not self.verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(data={"sub": db_user.phone_number}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
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

    def get_password_hash(self,password):
        return self.pwd_context.hash(password)

    def _get_user_by_phone_number_query(self, phone_number: str = None) -> Select:
        #consulta que devuelve solo los datos del usuario de la tabla usuario con phone_number
        query = (
            Select(self.database_client.users)
            .where(self.database_client.users.c.phone_number == phone_number)
        )
        return query

    def _get_user_by_user_id_query(self, user_id: int) -> Select:
        #consulta que devuelve solo los datos del usuario de la tabla usuario con id:user_id
        query = (
            Select(self.database_client.users)
            .where(self.database_client.users.c.user_id == user_id)
        )
        return query
