from SharmaBE.app.clients.db import DatabaseClient
from SharmaBE.app.schemas.usuarios import User
from SharmaBE.app.exceptions import UserAlreadyExists

from sqlalchemy.dialects.postgresql import insert




class UserService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def create_user(self, user_profile: User) -> int:
        data = dict(
            nombre=User.nombre,
            apellido1=User.apellido1,
            apellido2=User.apellido2,
            fecha_nacimiento=User.fecha_nacimiento,
            id_usuario=User.id_usuario,
            tarifa=User.tarifa,
            email=User.email,
            numero_telefono=User.numero_telefono,
            numero_pie=User.numero_pie,
            entradas_disponibles=User.entradas_disponibles,
            club_preferencia=User.club_preferencia
        )
        insert_stmt = (
            insert(self.database_client.usuarios)
            .values(**data)
            .returning(self.database_client.usuarios.c.id)
        )

        insert_stmt = insert_stmt.on_conflict_do_nothing(index_elements=["id"])
        res = await self.database_client.get_first(insert_stmt)
        if not res:
            raise UserAlreadyExists
        user_id = res[0]

        return user_id

