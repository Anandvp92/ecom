# Generated by Django 4.2.7 on 2023-12-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_productmodel_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='PRICE',
            field=models.FloatField(),
        ),
    ]
