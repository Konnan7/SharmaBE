import stripe
from app.config import STRIPE_SECRET_KEY
import logging

from app.schemas.payments import CreateStripePayment
from app.schemas.users import CreateStripeCustomer

logger = logging.getLogger(__name__)

stripe.api_key = STRIPE_SECRET_KEY

source = 'tok_visa'  # Este debería ser un token real obtenido desde el frontend


def create_stripe_payment(stripe_payment: CreateStripePayment):
    # try:
        logger.debug(f"Creando Stripe payment (previo)")

        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_payment.amount,  # Monto en centavos (ej. 2000 = $20.00)
            currency=stripe_payment.currency,
            # payment_method_types=stripe_payment.payment_method_types,
        )
        logger.debug(f"Creando Stripe payment: {payment_intent}")

        print('ID del PaymentIntent:', payment_intent.id)
        return payment_intent
    # except Exception as e:
    #     logger.debug(f"Fallo creando el Stripe payment")
    #
    #     print('Error creando el PaymentIntent:', e)


def create_stripe_customer(stripe_customer: CreateStripeCustomer):
    customer_create = stripe.Customer.create(
        name=stripe_customer.name,
        email=stripe_customer.email,
        phone=stripe_customer.phone
    )
    return customer_create


