import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


class CartHandler:

    def checkout_cart(self, amount: float, currency: str) -> str:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )

        return intent.client_secret
