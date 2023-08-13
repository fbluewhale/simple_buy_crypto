# Generated by Django 4.2.4 on 2023-08-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='purchase_price',
            field=models.BigIntegerField(default=0, verbose_name='Crypto purchase price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='sale_price',
            field=models.BigIntegerField(default=0, verbose_name='Crypto sales price'),
            preserve_default=False,
        ),
    ]
