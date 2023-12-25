from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from shop.handlers.cart_handler import CartHandler
from shop.handlers.currency_handler import CurrencyHandler
from shop.handlers.discount_handler import DiscountHandler
from shop.handlers.item_handler import ItemHandler
from shop.handlers.tax_handler import TaxHandler


class BuyItemView(View):
    """View покупки одного товара"""
    def get(self, request, *args, **kwargs):
        session_id = ItemHandler().checkout_item(kwargs.get('pk'))

        return JsonResponse({'id': session_id}, status=200)


class ViewItemView(View):
    """View просмотра деталей товара"""
    def get(self, request, *args, **kwargs):
        item = ItemHandler().get_item(kwargs.get('pk'))

        return render(request, 'shop/view_item.html', {'item': item})


class ListItemsView(View):
    """View просмотра списка товаров и оформления заказа"""
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


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutCartView(View):
    """View оформления заказа корзины"""
    def post(self, request, *args, **kwargs):
        stripe_prices = request.POST['stripe_prices'].split(',')
        discounts = request.POST['discounts'].split(',')
        currency = request.POST['currency']

        session_id = CartHandler().checkout_cart(stripe_prices, discounts, currency)

        return JsonResponse({'id': session_id}, status=200)
