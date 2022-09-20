# Generated by Django 4.1 on 2022-08-29 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buyer_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='ecommerce.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
