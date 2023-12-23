import stripe
from django.conf import settings

from shop.models import Item

stripe.api_key = settings.STRIPE_API_KEY


class ItemHandler:
    def checkout_item(self, item_id: int) -> str:
        item = Item.objects.get(id=item_id)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': item.price_stripe,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.CURRENT_DOMAIN + '/payment/success.html',
            cancel_url=settings.CURRENT_DOMAIN + '/payment/cancel.html',
        )

        return checkout_session.id

    def get_item(self, item_id: int) -> Item:
        return Item.objects.get(id=item_id)
