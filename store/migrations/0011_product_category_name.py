# Generated by Django 3.1.7 on 2021-03-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
