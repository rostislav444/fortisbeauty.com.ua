# Generated by Django 3.1.7 on 2021-06-16 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productdescriptionimages',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description_images', to='shop.variant', verbose_name='Обьем'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='shop.brand', verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='shop.categories', verbose_name='Категория товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='shop.country', verbose_name='Стнрана'),
        ),
        migrations.AddField(
            model_name='product',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='shop.brandseries', verbose_name='Серия бренда'),
        ),
        migrations.AddField(
            model_name='googletaxonomycategories',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.googletaxonomy'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categorychildrel',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_category', to='shop.categories'),
        ),
        migrations.AddField(
            model_name='categorychildrel',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_rel', to='shop.categories'),
        ),
        migrations.AddField(
            model_name='categories',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.categories', verbose_name='родительская катгория'),
        ),
        migrations.AddField(
            model_name='categories',
            name='taxonomy',
            field=models.ForeignKey(help_text='Таксономия Google', null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.googletaxonomycategories'),
        ),
        migrations.AddField(
            model_name='brandseries',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='shop.brand'),
        ),
        migrations.AddField(
            model_name='brandcategorytext',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.brand'),
        ),
        migrations.AddField(
            model_name='brandcategorytext',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.categories'),
        ),
        migrations.AddField(
            model_name='brandbanner',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='shop.brand'),
        ),
        migrations.AlterUniqueTogether(
            name='brandcategorytext',
            unique_together={('brand', 'category')},
        ),
    ]
