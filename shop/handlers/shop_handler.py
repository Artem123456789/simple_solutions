import stripe
from django.conf import settings

from shop.models import Item

stripe.api_key = settings.STRIPE_API_KEY


class ShopHandler:
    def checkout_item(self, item_id: int):
        item = Item.objects.get(id=item_id)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': item.price_stripe,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://google.com',
            cancel_url='https://google.com',
        )

        return checkout_session

    def get_item(self, item_id: int):
        return Item.objects.get(id=item_id)
