# Generated by Django 3.2.9 on 2021-11-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccomerce', '0003_alter_product_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
