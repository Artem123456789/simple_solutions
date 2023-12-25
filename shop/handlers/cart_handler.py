from typing import List

import stripe
from django.conf import settings

from shop.models import (
    Item,
    Discount,
    Order,
    Currency,
)

stripe.api_key = settings.STRIPE_API_KEY


class CartHandler:

    def checkout_cart(self, stripe_prices: List[str], discounts: List[str], currency: str) -> str:
        """Оформление заказа корзины"""
        items = Item.objects.filter(price_stripe__in=stripe_prices)
        discounts = Discount.objects.filter(stripe_id__in=discounts)
        currency_model = Currency.objects.get(code=currency)

        order = Order(currency=currency_model)
        order.save()

        order.items.add(*items)
        order.discounts.add(*discounts)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price,
                    'quantity': 1,
                } for price in stripe_prices
            ],
            discounts=[
                {
                    'coupon': discount,
                } for discount in discounts
            ],
            mode='payment',
            currency=currency,
            success_url=settings.CURRENT_DOMAIN + '/static/success.html',
            cancel_url=settings.CURRENT_DOMAIN + '/static/cancel.html',
        )

        return checkout_session.id
