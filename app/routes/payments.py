from fastapi import APIRouter, HTTPException

import json
import logging
import stripe
import os
from dotenv import load_dotenv


from app.schemas.rates import Rates, RateList
from app.schemas.payments import CreateStripePayment, PaymentCreate
from app.schemas.tickets import TicketCreate

from app.services.payments import PaymentService
from app.services.tickets import TicketService

from app.clients.db import DatabaseClient

from app.stripe_dependencies import create_stripe_payment
from app.dependencies import calculate_total_cost, verify_token

load_dotenv()

logger = logging.getLogger(__name__)
stripe.api_key = os.getenv("STRIPE_PUBLISHABLE_KEY")


def create_payments_router(database_client: DatabaseClient) -> APIRouter:
    payment_router = APIRouter()
    payment_service = PaymentService(database_client)
    ticket_service = TicketService(database_client)

    #tener POST y GET
    @payment_router.post("/purchase")
    async def create_purchase(list_of_products: list[Rates], token: str):
        token_data = verify_token(token)
        # Calcula el coste total de la cesta de la compra
        logger.debug(f"Datos token: {token_data}")

        total_cost = calculate_total_cost(list_of_rates=list_of_products)
        logger.debug(f"Coste total: {total_cost}")

        logger.debug(f"Creando objeto de Stripe Payment: {CreateStripePayment(amount=total_cost)}")

        stripe_payment = create_stripe_payment(stripe_payment=CreateStripePayment(amount=total_cost))
        logger.debug(f"Objeto Stripe de payment: {stripe_payment}")

        stripe_to_payment = PaymentCreate(amount=stripe_payment.amount,
                                          currency=stripe_payment.currency,
                                          description=stripe_payment.description,
                                          external_payment_id=stripe_payment.id)

        logger.debug(f"Objeto de PaymentCreate: {stripe_to_payment}")

        # Crear Payment en tabla local con los datos de stripe - DONE
        payment = await PaymentService.create_payment(stripe_payment)
        await stripe.PaymentIntent.confirm(payment.id, )
        logger.debug(f"Objeto de Payment para la BBDD: {payment}")

        # Crear tickets con los datos del payment con TicketCreate (rate_snapshot, status, ticket_id) y
        # necesito el token de identificacion
        list_of_tickets = []
        for product in list_of_products:
            logger.debug(f"Producto a añadir en BBDD tickets: {product}")

            product_json = json.dumps(product, indent=4)
            ticket = TicketCreate(rate_snapshot=product_json, status="Available", payment_id=payment.id)
            new_ticket = await ticket_service.create_ticket(phone_number=token_data.phone_number, ticket=ticket)
            list_of_tickets.append(new_ticket)

        return list_of_tickets

    # @payment_router.post("/stripe/payment/")
    # def create_stripe_payment_endpoint(amount: int, currency: str, source: str, description: str):
    #     charge = create_stripe_payment(amount, currency, source, description)
    #     payment_service.create_payment(price=amount, )
    #     if charge:
    #         return {"status": "success", "charge": charge}
    #     else:
    #         raise HTTPException(status_code=400, detail="Payment failed")


    return payment_router
