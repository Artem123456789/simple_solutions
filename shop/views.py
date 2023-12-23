from django.shortcuts import render
from django.views import View

from shop.handlers.shop_handler import ShopHandler


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        ShopHandler().checkout_item(kwargs.get('pk'))

        return render(request, 'shop/buy_item.html')


class ViewItemView(View):
    def get(self, request, *args, **kwargs):
        item = ShopHandler().get_item(kwargs.get('pk'))

        return render(request, 'shop/view_item.html', {'item': item})
