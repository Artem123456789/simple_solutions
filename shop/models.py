from django.db import models
from django.utils.translation import gettext as _


class Item(models.Model):
    name = models.CharField(max_length=100)
    price_stripe = models.CharField(max_length=100)
    price_for_view = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.name
