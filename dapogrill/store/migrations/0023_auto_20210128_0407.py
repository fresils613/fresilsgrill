# Generated by Django 3.1.5 on 2021-01-28 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20210128_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('Order On The Way', 'Order On The way'), ('Order Not Yet Recieved', 'Order Not Yet Recieved')], default='Order Not Yet Recieved', max_length=100),
        ),
    ]
