from typing import Iterable

from shop.models import Discount


class DiscountHandler:
    def get_all_items(self) -> Iterable[Discount]:
        return Discount.objects.all()
