# Generated by Django 5.0 on 2023-12-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_order_discount_order_discounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='stripe_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
