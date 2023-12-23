from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from shop.handlers.shop_handler import ItemHandler


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        session_id = ItemHandler().checkout_item(kwargs.get('pk'))

        return JsonResponse({'id': session_id}, status=200)


class ViewItemView(View):
    def get(self, request, *args, **kwargs):
        item = ItemHandler().get_item(kwargs.get('pk'))

        return render(request, 'shop/view_item.html', {'item': item})
