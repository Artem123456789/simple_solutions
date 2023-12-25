from typing import Iterable

from shop.models import Currency


class CurrencyHandler:
    def get_all_items(self) -> Iterable[Currency]:
        return Currency.objects.all()
