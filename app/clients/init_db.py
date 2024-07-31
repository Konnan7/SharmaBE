from models.base import Base
from sqlalchemy import inspect
from models.clubs import Clubs
from models.rates import Rates
from models.payments import Payments

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')



def init_db(engine, session):

    Base.metadata.create_all(bind=engine)

    # Crear una sesión
    db = session

    # Insertar datos iniciales de Clubs y Rates

    #Clubs - DONE
    club1 = Clubs(club_id=1, schedule="Every Day", location="Gava", name="Sharma Gavà", status="Active")
    club2 = Clubs(club_id=2, schedule="Every Day", location="Barcelona", name="Sharma BCN", status="Active")
    club3 = Clubs(club_id=3, schedule="Every Day", location="Madrid", name="Sharma Madrid", status="Active")
    club4 = Clubs(club_id=4, schedule="Every Day", location="Universal", name="Todos los centros Sharma", status="Active")


    #Rates - Pending all rates
    rate1 = Rates(rate_id=1, type="Entrada puntual mañana", amount=1000, club_id=1)
    rate2 = Rates(rate_id=2, type="Entrada puntual reducida", amount=1100, club_id=1)
    rate3 = Rates(rate_id=3, type="Entrada puntual normal", amount=1400, club_id=1)

    rate13 = Rates(rate_id=13, type="Pack 10 entradas normal", amount=13500, club_id=1)
    rate14 = Rates(rate_id=14, type="Pack 10 entradas reducida", amount=11500, club_id=1)

    rate15 = Rates(rate_id=15, type="Abono Mensual Normal", amount=6200, club_id=1)
    rate16 = Rates(rate_id=16, type="Abono Mensual Reducida", amount=57500, club_id=1)
    rate17 = Rates(rate_id=17, type="Abono Mensual Mañana", amount=46500, club_id=1)

    rate18 = Rates(rate_id=18, type="Bono 30 dias Normal", amount=7000, club_id=1)
    rate19 = Rates(rate_id=19, type="Bono 30 dias Reducida", amount=6500, club_id=1)
    rate20 = Rates(rate_id=20, type="Bono 30 dias Mañana", amount=5000, club_id=1)

    rate4 = Rates(rate_id=4, type="Entrada puntual mañana", amount=1000, club_id=2)
    rate5 = Rates(rate_id=5, type="Entrada puntual reducida", amount=1100, club_id=2)
    rate6 = Rates(rate_id=6, type="Entrada puntual normal", amount=1400, club_id=2)
    rate10 = Rates(rate_id=10, type="Pack 10 entradas", amount=12000, club_id=2)
    rate11 = Rates(rate_id=11, type="Pack 10 entradas reducida", amount=10000, club_id=2)

    rate7 = Rates(rate_id=7, type="Entrada puntual mañana", amount=1300, club_id=3)
    rate8 = Rates(rate_id=8, type="Entrada puntual reducida", amount=1300, club_id=3)
    rate9 = Rates(rate_id=9, type="Entrada puntual normal", amount=1500, club_id=3)

    rate21 = Rates(rate_id=21, type="Abono Mensual Normal Multigym", amount=6700, club_id=4)
    rate22 = Rates(rate_id=22, type="Abono Mensual Reducida Multigym", amount=6250, club_id=4)
    rate23 = Rates(rate_id=23, type="Abono Mensual Mañana Multigym", amount=4700, club_id=4)






    payment1 = Payments(amount=10, currency="eur", stripe_id=1, description="Description test")
    payment2 = Payments(amount=50, currency="eur", stripe_id=2, description="Description test")
    payment3 = Payments(amount=100, currency="eur", stripe_id=3, description="Description test")

    db.add(club1)
    db.add(club2)
    db.add(club3)
    db.add(club4)

    db.add(rate1)
    db.add(rate2)
    db.add(rate3)
    db.add(rate4)
    db.add(rate5)
    db.add(rate6)
    db.add(rate7)
    db.add(rate8)
    db.add(rate9)
    db.add(rate10)
    db.add(rate11)
    #db.add(rate12)
    db.add(rate13)
    db.add(rate14)
    db.add(rate15)
    db.add(rate16)
    db.add(rate17)
    db.add(rate18)
    db.add(rate19)
    db.add(rate20)
    db.add(rate21)
    db.add(rate22)
    db.add(rate23)

    db.add(payment1)
    db.add(payment2)
    db.add(payment3)

    # Confirmar la transacción
    db.commit()

    # Cerrar la sesión
    db.close()


