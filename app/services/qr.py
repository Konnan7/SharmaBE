from app.clients.db import DatabaseClient



class QRService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client
