# Generated by Django 4.2.7 on 2023-12-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_productmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='PRICE',
            field=models.DecimalField(decimal_places=4, max_digits=25),
        ),
    ]
