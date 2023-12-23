from django.contrib import admin

from shop.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)