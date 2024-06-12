import logging

from fastapi import APIRouter
import qrcode
from io import BytesIO
from fastapi.responses import StreamingResponse

logger = logging.getLogger(__name__)


def create_router() -> APIRouter:
    router = APIRouter()

    @router.post("/generate_qr")
    def generate_qr(data: str):
        # Generar el código QR
        qr = qrcode.make(data)
        buf = BytesIO() #pendiente de ver que hace esto
        qr.save(buf)
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")

    return router
