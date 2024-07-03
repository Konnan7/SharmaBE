import logging

from app.exception_handlers import UserNotFound
from fastapi import APIRouter
from models.users import Users
from app.services.users import UserService
from app.clients.db import DatabaseClient
from app.schemas.users import User


from typing import Optional

logger = logging.getLogger(__name__)


def create_user_router(database_client: DatabaseClient) -> APIRouter:
    user_router = APIRouter()
    user_service = UserService(database_client)

    @user_router.post("/register", status_code=201)
    async def add_user(user_profile: User, password:str):
        user_id = await user_service.create_user(user_profile, password)
        return user_id

    @user_router.post("/login", response_model=Token)
    def login_for_access_token(user: UserCreate, db: Session = Depends(get_db)):
        db_user = db.query(User).filter(User.username == user.username).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": db_user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    @user_router.get("/{user_id}")
    async def get_user(user_id: Optional[int]) -> User:
        user = await user_service.get_user_by_id(user_id)
        return user



    @user_router.on_event("startup")
    async def startup():
        await database_client.connect()

    @user_router.on_event("shutdown")
    async def shutdown():
        await database_client.disconnect()

    return user_router
