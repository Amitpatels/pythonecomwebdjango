# Generated by Django 3.0.5 on 2020-05-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
    ]
