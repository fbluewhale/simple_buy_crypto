# Generated by Django 4.2.4 on 2023-08-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0006_alter_order_amount_alter_order_purchase_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="sale_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=18,
                verbose_name="Crypto sales price",
            ),
        ),
    ]
