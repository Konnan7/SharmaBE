from create_app import create_application
from fastapi.middleware.cors import CORSMiddleware


app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto para permitir solo dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
