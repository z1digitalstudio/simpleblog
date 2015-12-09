# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Blog Category', 'verbose_name_plural': 'Blog Categories'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-publication_date'], 'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.AddField(
            model_name='category',
            name='seo_description',
            field=models.CharField(max_length=155, null=True, verbose_name='Description (SEO)', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='seo_title',
            field=models.CharField(max_length=68, null=True, verbose_name='Title (SEO)', blank=True),
        ),
    ]
