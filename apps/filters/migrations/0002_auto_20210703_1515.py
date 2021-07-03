# Generated by Django 3.1.7 on 2021-07-03 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attrs', to='shop.product'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='value',
            field=models.ManyToManyField(blank=True, related_name='product_attrs', to='filters.AttributeValue'),
        ),
        migrations.AddField(
            model_name='categoryattributevalue',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_values', to='filters.categoryattribute', verbose_name='Связь атрибутов с категрией'),
        ),
        migrations.AddField(
            model_name='categoryattributevalue',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_values', to='filters.attributevalue', verbose_name='Атрибут'),
        ),
        migrations.AddField(
            model_name='categoryattribute',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='filters.attribute', verbose_name='Группа атрибутов'),
        ),
        migrations.AddField(
            model_name='categoryattribute',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='shop.categories', verbose_name='Катгория'),
        ),
        migrations.AddField(
            model_name='categoryattribute',
            name='values',
            field=models.ManyToManyField(through='filters.CategoryAttributeValue', to='filters.AttributeValue'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='values', to='filters.attribute'),
        ),
        migrations.AlterUniqueTogether(
            name='productattribute',
            unique_together={('parent', 'attribute')},
        ),
        migrations.AlterUniqueTogether(
            name='categoryattributevalue',
            unique_together={('parent', 'value')},
        ),
        migrations.AlterUniqueTogether(
            name='categoryattribute',
            unique_together={('parent', 'attribute')},
        ),
        migrations.AlterUniqueTogether(
            name='attributevalue',
            unique_together={('parent', 'name')},
        ),
    ]