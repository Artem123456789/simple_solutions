from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from shop.handlers.shop_handler import ShopHandler


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        session = ShopHandler().checkout_item(kwargs.get('pk'))

        return JsonResponse({'id': session.id}, status=200)


class ViewItemView(View):
    def get(self, request, *args, **kwargs):
        item = ShopHandler().get_item(kwargs.get('pk'))

        return render(request, 'shop/view_item.html', {'item': item})
