# Generated by Django 3.1.5 on 2021-01-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210127_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
