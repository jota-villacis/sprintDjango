# Generated by Django 3.2.9 on 2021-11-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccomerce', '0004_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]
