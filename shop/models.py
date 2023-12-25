from django.db import models
from django.utils.translation import gettext as _


class Item(models.Model):
    name = models.CharField(max_length=100)
    price_stripe = models.CharField(max_length=100, verbose_name=_('Идентификатор цены товара в Stripe'))
    price_for_view = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_('Цена товара для отображения'))
    description = models.TextField()

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)
    stripe_id = models.CharField(max_length=100, default='', verbose_name=_('Идентификатор скидки в Stripe'))
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


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Валюта')
        verbose_name_plural = _('Валюты')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discounts = models.ManyToManyField(Discount)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return str(self.id)
