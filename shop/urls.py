from django.urls import path

from shop.views import (
    BuyItemView,
    ViewItemView,
)

urlpatterns = [
    path('buy/<int:pk>/', BuyItemView.as_view(), name='buy'),
    path('view/<int:pk>/', ViewItemView.as_view(), name='view'),
]
