import stripe
import os
from dotenv import load_dotenv

load_dotenv('.env-local')

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# stripe.api_key = "sk_test_51PdWGTRoAMcu4xXCHGnTEqKnxCBDf7Wn97acgoWioTluLWKqZuwcm1Xq7IdBSfNv36DNlDoMzT8qUdaI2obnycmV00QaHQwlYk"

customer_create= stripe.Customer.create(
  name="Jenny Rosen",
  email="jennyrosen@example.com",
  phone="606582907"
)
#Añadir Stripe.id a tabla de usuarios
print(customer_create)

payment_intent = stripe.PaymentIntent.create(
  amount=1099,
  currency="eur",
    payment_method_types=["card"],
    customer=customer_create
)



# print(payment_intent)