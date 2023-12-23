from django.urls import path

from shop.views import BuyItemView

urlpatterns = [
    path('buy/<int:pk>/', BuyItemView.as_view(), name='buy'),
]
