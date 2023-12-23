from django.shortcuts import render
from django.views import View

from shop.handlers.shop_handler import ShopHandler


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        ShopHandler().checkout_item(kwargs.get('pk'))

        return render(request, 'shop/buy_item.html')
