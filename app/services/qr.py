<<<<<<< HEAD
from SharmaBE.app.clients.db import DatabaseClient
=======
from app.clients.db import DatabaseClient
>>>>>>> ff1a877 (Añadido repositorio de BBDD)


class QRService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client
