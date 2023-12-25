from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from shop.handlers.cart_handler import CartHandler
from shop.handlers.currency_handler import CurrencyHandler
from shop.handlers.discount_handler import DiscountHandler
from shop.handlers.item_handler import ItemHandler
from shop.handlers.tax_handler import TaxHandler


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
        taxes = TaxHandler().get_all_items()
        currencies = CurrencyHandler().get_all_items()

        return render(
            request,
            'shop/list_items.html',
            {'items': items, 'discounts': discounts, 'taxes': taxes, 'currencies': currencies}
        )


class CheckoutCartView(View):
    def get(self, request, *args, **kwargs):
        stripe_prices = request.GET['stripe_prices'].split(',')
        discounts = request.GET['discounts'].split(',')
        currency = request.GET['currency']

        session_id = CartHandler().checkout_cart(stripe_prices, discounts, currency)

        return JsonResponse({'id': session_id}, status=200)
