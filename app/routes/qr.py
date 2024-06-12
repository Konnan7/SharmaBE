import logging

from fastapi import APIRouter
import qrcode

logger = logging.getLogger(__name__)


def create_router() -> APIRouter:
    router = APIRouter()

    @router.post("/generate_qr")
    def generate_qr(data: str):
        # Generar el código QR
        qr = qrcode.make(data)
        buf = BytesIO()
        qr.save(buf, format='PNG')
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")

    return router
