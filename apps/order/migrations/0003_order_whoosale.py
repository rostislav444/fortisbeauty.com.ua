# Generated by Django 3.1.7 on 2021-06-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210616_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='whoosale',
            field=models.BooleanField(default=False, verbose_name='Оптовый заказ'),
        ),
    ]
