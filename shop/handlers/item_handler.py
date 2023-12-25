from typing import Iterable

import stripe
from django.conf import settings

from shop.models import Item

stripe.api_key = settings.STRIPE_API_KEY


class ItemHandler:
    def checkout_item(self, item_id: int) -> str:
        """Оформление заказа для одного товара"""
        item = Item.objects.get(id=item_id)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': item.price_stripe,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.CURRENT_DOMAIN + '/static/success.html',
            cancel_url=settings.CURRENT_DOMAIN + '/static/cancel.html',
        )

        return checkout_session.id

    def get_item(self, item_id: int) -> Item:
        return Item.objects.get(id=item_id)

    def get_all_items(self) -> Iterable[Item]:
        return Item.objects.all()
