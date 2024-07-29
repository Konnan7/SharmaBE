import stripe
import os
from dotenv import load_dotenv

from app.schemas.payments import CreateStripePayment

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

source = 'tok_visa'  # Este debería ser un token real obtenido desde el frontend


def create_stripe_payment(stripe_payment: CreateStripePayment):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_payment.amount,  # Monto en centavos (ej. 2000 = $20.00)
            currency=stripe_payment.currency,
            payment_method_types=stripe_payment.payment_method_types,
        )
        print('ID del PaymentIntent:', payment_intent.id)
        return payment_intent
    except Exception as e:
        print('Error creando el PaymentIntent:', e)
