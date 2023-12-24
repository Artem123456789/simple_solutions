from django.urls import path

from shop.views import (
    BuyItemView,
    ViewItemView,
    ListItemsView,
    CheckoutCartView,
)

urlpatterns = [
    path('buy/<int:pk>/', BuyItemView.as_view(), name='buy'),
    path('view/<int:pk>/', ViewItemView.as_view(), name='view'),
    path('', ListItemsView.as_view(), name='root'),
    path('checkout/', CheckoutCartView.as_view(), name='checkout'),
]
