import stripe
stripe.api_key = "sk_test_51PdWGTRoAMcu4xXCHGnTEqKnxCBDf7Wn97acgoWioTluLWKqZuwcm1Xq7IdBSfNv36DNlDoMzT8qUdaI2obnycmV00QaHQwlYk"

customer_create= stripe.Customer.create(
  name="Jenny Rosen",
  email="jennyrosen@example.com",
)
#Añadir Stripe.id a tabla de usuarios
print(customer_create.id)

payment_intent = stripe.PaymentIntent.create(
  amount=1099,
  currency="eur",
    payment_method_types=["card"],
    customer=customer_create
)

print(payment_intent)