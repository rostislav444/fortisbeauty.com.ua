# Generated by Django 3.1.7 on 2021-06-16 13:01

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('seo_title', models.CharField(blank=True, help_text='До 70 символов', max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.TextField(blank=True, help_text='До 300 символов', max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('seo_keywords', models.TextField(blank=True, help_text='До 255 символов', max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='Иденитификатор')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0, verbose_name='№')),
                ('image', models.FileField(blank=True, max_length=1024, null=True, upload_to='', verbose_name='Изображение')),
                ('image_thmb', models.JSONField(blank=True, default=dict, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('discount', models.PositiveIntegerField(default=0)),
                ('discount_whoosale', models.PositiveIntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('disable', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BrandBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_pc', models.ImageField(upload_to='', verbose_name='Баннер для ПК')),
                ('image_mob', models.ImageField(upload_to='', verbose_name='Баннер для мобильных')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки')),
            ],
            options={
                'verbose_name': 'Бренд: баннер',
                'verbose_name_plural': 'Бренды: баннеры',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='BrandCategoryText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='BrandSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='Иденитификатор')),
            ],
            options={
                'verbose_name': 'Бренд: Cерия',
                'verbose_name_plural': 'Бренды: Cерии',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('seo_title', models.CharField(blank=True, help_text='До 70 символов', max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.TextField(blank=True, help_text='До 300 символов', max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('seo_keywords', models.TextField(blank=True, help_text='До 255 символов', max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='Иденитификатор')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0, verbose_name='№')),
                ('image', models.FileField(blank=True, max_length=1024, null=True, upload_to='', verbose_name='Изображение')),
                ('image_thmb', models.JSONField(blank=True, default=dict, null=True)),
                ('human', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Понятное названиме')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CategoryChildRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('COMMENT', 'Comment'), ('QUESTION', 'Question')], default='COMMENT', max_length=10)),
                ('rate', models.PositiveIntegerField(blank=True, choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=5, null=True, verbose_name='Оцените товар')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('advantages', models.CharField(blank=True, max_length=1200, null=True, verbose_name='Преимущества')),
                ('disadvantages', models.CharField(blank=True, max_length=1200, null=True, verbose_name='Недостатки')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('dislike', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='Иденитификатор')),
            ],
            options={
                'verbose_name': 'Продукт: Страна производитель',
                'verbose_name_plural': 'Продукт: Страны производители',
            },
        ),
        migrations.CreateModel(
            name='GoogleTaxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='https://www.google.com/basepages/producttype/taxonomy-with-ids.ru-RU.txt', max_length=1500)),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('limit', models.CharField(blank=True, default='Красота и здоровье', help_text='Для добавдения нескольких категорий, пишите их через запятую с пробелом.', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Таксономия Google - Загрузка',
                'verbose_name_plural': 'Таксономия Google - Загрузка',
            },
        ),
        migrations.CreateModel(
            name='GoogleTaxonomyCategories',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1500)),
            ],
            options={
                'verbose_name': 'Таксономия Google - Категории',
                'verbose_name_plural': 'Таксономия Google - Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_childs', models.BooleanField(default=False, verbose_name='Перевод')),
                ('seo_title', models.CharField(blank=True, help_text='До 70 символов', max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.TextField(blank=True, help_text='До 300 символов', max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('seo_keywords', models.TextField(blank=True, help_text='До 255 символов', max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('prescription', models.TextField(blank=True, null=True, verbose_name='Назначение')),
                ('application', models.TextField(blank=True, null=True, verbose_name='Способ применения')),
                ('composition', models.TextField(blank=True, null=True, verbose_name='Состав')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('description_text', models.TextField(blank=True, null=True, verbose_name='Описание (только текст)')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.CharField(blank=True, max_length=500, verbose_name='Идентификатор (авто)')),
                ('human', models.CharField(blank=True, max_length=500, null=True, verbose_name='Понятное название (для чего продукт)')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки')),
                ('update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('unit', models.CharField(blank=True, max_length=500, null=True, verbose_name='Еденица измерения вариантов продукта')),
                ('views', models.PositiveIntegerField(blank=True, default=0, verbose_name='Просмотров')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукт',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='ProductDescriptionImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0, verbose_name='№')),
                ('image', models.FileField(blank=True, max_length=1024, null=True, upload_to='', verbose_name='Изображение')),
                ('image_thmb', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='Иденитификатор')),
                ('unit', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ед. измер.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=250, null=True, verbose_name='Значение')),
                ('price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена')),
                ('discount_price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена (скидка)')),
                ('whoosale_price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Оптовая цена')),
                ('discount_whoosale_price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Оптовая цена (скидка)')),
                ('code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Артикул')),
                ('barcode', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Штрихкод')),
                ('stock', models.PositiveIntegerField(blank=True, default=1, verbose_name='Остаток')),
                ('update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('views', models.PositiveIntegerField(blank=True, default=0, verbose_name='Просмотров')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='shop.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт: Вариант',
                'verbose_name_plural': 'Продукт: Варианты',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='VariantImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.PositiveIntegerField(default=0, verbose_name='№')),
                ('image', models.FileField(blank=True, max_length=1024, null=True, upload_to='', verbose_name='Изображение')),
                ('image_thmb', models.JSONField(blank=True, default=dict, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.variant', verbose_name='Обьем')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('dislike', models.PositiveIntegerField(default=0)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='shop.comment')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.reply')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
