# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('image', models.ImageField(upload_to=b'blog/images/', verbose_name='Image')),
                ('intro', models.TextField(verbose_name='Introduction')),
                ('content', models.TextField(verbose_name='Content')),
                ('published', models.BooleanField(default=False, db_index=True, verbose_name='Published')),
                ('publication_date', models.DateField(verbose_name='Publication Date', db_index=True)),
                ('seo_title', models.CharField(max_length=68, null=True, verbose_name='Title (SEO)', blank=True)),
                ('seo_description', models.CharField(max_length=155, null=True, verbose_name='Description (SEO)', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='Category', to='simpleblog.Category')),
            ],
        ),
    ]
