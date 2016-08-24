# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0003_entryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Category', blank=True, to='simpleblog.Category', null=True),
        ),
    ]
