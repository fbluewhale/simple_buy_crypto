# Generated by Django 4.2.4 on 2023-08-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coin", "0002_remove_coin_abbreviation_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="coin",
            name="abbreviation_name",
            field=models.CharField(
                default="", max_length=20, verbose_name="abbreviation name"
            ),
            preserve_default=False,
        ),
    ]
