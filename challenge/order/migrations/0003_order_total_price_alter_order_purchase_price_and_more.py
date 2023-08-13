# Generated by Django 4.2.4 on 2023-08-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_remove_order_price_order_purchase_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.BigIntegerField(default=0, verbose_name="Crypto sales price"),
        ),
        migrations.AlterField(
            model_name="order",
            name="purchase_price",
            field=models.BigIntegerField(
                default=0, verbose_name="Crypto purchase price"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="sale_price",
            field=models.BigIntegerField(default=0, verbose_name="Crypto sales price"),
        ),
    ]
