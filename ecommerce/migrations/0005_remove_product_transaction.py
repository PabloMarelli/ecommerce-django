# Generated by Django 4.1 on 2022-09-01 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_tag_product_price_transaction_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='transaction',
        ),
    ]
