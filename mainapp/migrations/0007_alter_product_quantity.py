# Generated by Django 3.2.10 on 2022-01-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_product_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=0, verbose_name="количество на складе"),
        ),
    ]
