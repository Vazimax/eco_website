# Generated by Django 3.1.7 on 2021-03-16 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210316_1452'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdsress',
            new_name='ShippingAddress',
        ),
    ]
