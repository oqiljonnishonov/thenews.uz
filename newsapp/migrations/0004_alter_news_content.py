# Generated by Django 4.2.13 on 2024-06-24 18:12

import ckeditor.fields
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_category_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(default=datetime.date, verbose_name='Content'),
            preserve_default=False,
        ),
    ]
