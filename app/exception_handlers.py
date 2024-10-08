from fastapi import Request,FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import UserNotFound,UserAlreadyExists
from sqlalchemy.exc import IntegrityError

import logging


logger = logging.getLogger(__name__)


def add_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(UserNotFound)
    async def handle_user_not_found_exception(request: Request, exc: UserNotFound):
        logger.error(f"Invalid user_id {exc.user_id} was requested ")
        return JSONResponse(status_code=404, content="User does not exist")

    @app.exception_handler(UserAlreadyExists)
    async def handle_user_not_found_exception(request: Request, exc: UserNotFound):
        logger.error(f"Tried to insert user that already exists ")
        return JSONResponse(status_code=400, content="User already exists")

    @app.exception_handler(IntegrityError)
    async def handle_user_not_found_exception(request: Request, exc: UserNotFound):
        logger.error(f"Encountered integrity error when inserting user ")
        return JSONResponse(status_code=400, content="User conflicts with existing user")

    return None
