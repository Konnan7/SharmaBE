from models.base import Base
from sqlalchemy import inspect
from models.clubs import Clubs
from models.rates import Rates

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')



def init_db(engine, session):

    Base.metadata.create_all(bind=engine)

    # Crear una sesión
    db = session

    # Insertar datos iniciales de Clubs y Rates
    club1 = Clubs(club_id=1,schedule="Every Day", location="Gava", name="Sharma Gavà", status="Active")
    club2 = Clubs(club_id=2,schedule="Every Day", location="Barcelona", name="Sharma BCN", status="Active")
    club3 = Clubs(club_id=3,schedule="Every Day", location="Madrid", name="Sharma Madrid", status="Active")

    rate1 = Rates(rate_id=1,type="Early", price=12, club_id=1)
    rate2 = Rates(rate_id=2,type="Day", price=15, club_id=1)
    rate3 = Rates(rate_id=3,type="Member", price = 0, club_id=1)

    db.add(club1)
    db.add(club2)
    db.add(club3)

    db.add(rate1)
    db.add(rate2)
    db.add(rate3)

    # Confirmar la transacción
    db.commit()

    # Cerrar la sesión
    db.close()


