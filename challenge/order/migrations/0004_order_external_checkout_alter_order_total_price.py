# Generated by Django 4.2.4 on 2023-08-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_total_price_alter_order_purchase_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='external_checkout',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.BigIntegerField(default=0, verbose_name='order total price'),
        ),
    ]
