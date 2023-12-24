from typing import Iterable

from shop.models import Tax


class TaxesHandler:
    def get_all_items(self) -> Iterable[Tax]:
        return Tax.objects.all()
