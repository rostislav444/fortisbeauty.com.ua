# Generated by Django 3.1.7 on 2021-07-05 17:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whoosaletext',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст'),
        ),
    ]
