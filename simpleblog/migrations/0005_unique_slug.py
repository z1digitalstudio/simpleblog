# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def rename_duplicated_slugs(apps, schema_editor):
    Entry = apps.get_model("simpleblog", "Entry")
    entries = Entry.objects.all()
    modified = []
    for entry in entries:
        if entry.pk in modified:
            continue
        repeated = Entry.objects.exclude(pk=entry.pk).filter(slug=entry.slug)
        if repeated:
            n = 1
            for rep in repeated:
                rep.slug = "{0}-{1}".format(rep.slug, n)
                # Used to avoid signals
                Entry.objects.filter(pk=rep.pk).update(slug=rep.slug)
                modified.append(rep.pk)
                n += 1


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0004_auto_20160824_0757'),
    ]

    operations = [
        migrations.RunPython(rename_duplicated_slugs),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, verbose_name='Slug'),
        ),
    ]
