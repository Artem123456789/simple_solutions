from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from shop.handlers.discount_handler import DiscountHandler
from shop.handlers.shop_handler import ItemHandler
from shop.handlers.taxes_handler import TaxesHandler


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        session_id = ItemHandler().checkout_item(kwargs.get('pk'))

        return JsonResponse({'id': session_id}, status=200)


class ViewItemView(View):
    def get(self, request, *args, **kwargs):
        item = ItemHandler().get_item(kwargs.get('pk'))

        return render(request, 'shop/view_item.html', {'item': item})


class ListItemsView(View):
    def get(self, request, *args, **kwargs):
        items = ItemHandler().get_all_items()
        discounts = DiscountHandler().get_all_items()
        taxes = TaxesHandler().get_all_items()

        return render(
            request,
            'shop/list_items.html',
            {'items': items, 'discounts': discounts, 'taxes': taxes}
        )
