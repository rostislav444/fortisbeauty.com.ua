# Generated by Django 3.1.7 on 2021-07-05 17:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('title', models.CharField(default='Доставка', max_length=255, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Страница: Доставка',
                'verbose_name_plural': 'Страница: Доставка ',
            },
        ),
        migrations.CreateModel(
            name='PagePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('title', models.CharField(default='Оплата', max_length=255, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Страница: Оплата',
                'verbose_name_plural': 'Страница: Оплата',
            },
        ),
        migrations.CreateModel(
            name='PageTermsOfUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('title', models.CharField(default='Доставка', max_length=255, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Страница: Условия использования',
                'verbose_name_plural': 'Страница: Условия использования ',
            },
        ),
        migrations.DeleteModel(
            name='PagePaymentAndDelivery',
        ),
    ]