# Generated by Django 4.2.7 on 2023-12-11 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='imagepath',
            new_name='IMAGE',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='Rating',
            new_name='RATINGS',
        ),
    ]
