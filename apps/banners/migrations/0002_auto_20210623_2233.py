# Generated by Django 3.1.7 on 2021-06-23 19:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='image',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='image_thmb',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='num',
        ),
        migrations.AlterField(
            model_name='banner',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='link',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='BannerPC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0, verbose_name='№')),
                ('image_thmb', models.JSONField(blank=True, default=dict, null=True)),
                ('image', models.FileField(max_length=1024, upload_to='', verbose_name='Изображение PC')),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='banners.banner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BannerMobile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0, verbose_name='№')),
                ('image_thmb', models.JSONField(blank=True, default=dict, null=True)),
                ('image', models.FileField(max_length=1024, upload_to='', verbose_name='Изображение Мобильный')),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='banners.banner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]