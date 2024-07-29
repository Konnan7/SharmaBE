from fastapi import APIRouter, HTTPException

from app.schemas.rates import Rates, RateList
from app.schemas.payments import CreateStripePayment, PaymentCreate

from app.services.payments import PaymentService

from app.clients.db import DatabaseClient

from app.stripe_dependencies import create_stripe_payment
from app.dependencies import calculate_total_cost


def create_payments_router(database_client: DatabaseClient) -> APIRouter:
    payment_router = APIRouter()
    payment_service = PaymentService(database_client)

    #tener POST y GET
    @payment_router.post("/purchase")
    async def create_purchase(list_of_products: list[Rates]):
        # Calcula el coste total de la cesta de la compra
        total_cost = calculate_total_cost(list_of_rates=list_of_products)

        stripe_payment = create_stripe_payment(stripe_payment=CreateStripePayment(amount=total_cost))
        stripe_to_payment = PaymentCreate(amount=stripe_payment.amount,
                                          currency=stripe_payment.currency,
                                          description=stripe_payment.description,
                                          external_payment_id=stripe_payment.id)

        # Crear Payment en tabla local con los datos de stripe - DONE
        payment = await PaymentService.create_payment(stripe_payment)

        # Crear tickets con los datos del payment con TicketCreate (rate_snapshot, status, ticket_id) y
        # necesito el token de identificacion





    @payment_router.post("/stripe/payment/")
    def create_stripe_payment_endpoint(amount: int, currency: str, source: str, description: str):
        charge = create_stripe_payment(amount, currency, source, description)
        payment_service.create_payment(price=amount, )
        if charge:
            return {"status": "success", "charge": charge}
        else:
            raise HTTPException(status_code=400, detail="Payment failed")

    @staticmethod
    async def sum_total_cost(list_of_rates: RateList):
        pass

    @staticmethod
    async def create_payment_from_stripe(payment: StripePayment):
        pass


    return payment_router
