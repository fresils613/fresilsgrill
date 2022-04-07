# Generated by Django 3.1.5 on 2021-01-27 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Received', 'order Received'), ('Order Canceled', 'order Canceled')], default='order Canceled', max_length=100),
        ),
    ]