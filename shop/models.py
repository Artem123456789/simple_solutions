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


class Discount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = _('Скидка')
        verbose_name_plural = _('Скидки')

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = _('Налог')
        verbose_name_plural = _('Налоги')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return self.id
