# Generated by Django 4.1 on 2022-09-01 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_transaction_quantity_alter_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='status',
            new_name='active',
        ),
    ]
