# Generated by Django 3.1.7 on 2021-03-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210317_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]