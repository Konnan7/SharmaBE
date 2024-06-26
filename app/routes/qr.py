import logging

from fastapi import APIRouter
import qrcode
from io import BytesIO
from fastapi.responses import StreamingResponse

from app.services.qr import QRService
from app.schemas.qr import *

from app.clients.db import DatabaseClient

logger = logging.getLogger(__name__)


def create_qr_router(database_client:DatabaseClient) -> APIRouter:
    qr_router = APIRouter()
    qr_service = QRService(database_client)

    @qr_router.get("/generate_qr")
    def generate_qr(data: str):
        # Generar el código QR
        qr = qrcode.make(data)
        buf = BytesIO() #pendiente de ver que hace esto
        qr.save(buf)
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")

    return qr_router
