# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0002_auto_20151209_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'blog/images/', null=True, verbose_name='Image')),
                ('entry', models.ForeignKey(related_name='entries', verbose_name='Author', to='simpleblog.Entry')),
            ],
            options={
                'verbose_name': 'Entry image',
                'verbose_name_plural': 'Entry images',
            },
        ),
    ]
