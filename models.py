from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from simpleblog.managers import EntryManager


class Category(models.Model):
    name = models.CharField(
        _(u'Name'),
        max_length=200
    )
    slug = models.SlugField(
        _(u'Slug'),
        max_length=100,
        db_index=True
    )


class Entry(models.Model):
    title = models.CharField(
        _(u'Title'),
        max_length=200
    )
    slug = models.SlugField(
        _(u'Slug'),
        max_length=100,
        db_index=True
    )
    image = models.ImageField(
        _(u'Image'),
        upload_to='blog/images/'
    )
    intro = models.TextField(
        _(u'Introduction')
    )
    content = models.TextField(
        _(u'Content')
    )
    published = models.BooleanField(
        _(u'Published'),
        default=False,
        db_index=True
    )
    publication_date = models.DateField(
        _(u'Publication Date'),
        db_index=True
    )
    seo_title = models.CharField(
        _(u'Title (SEO)'),
        max_length=68,
        blank=True, null=True
    )
    seo_description = models.CharField(
        _(u'Description (SEO)'),
        max_length=155,
        blank=True, null=True
    )
    created = models.DateTimeField(
        _(u'Created'),
        auto_now_add=True
    )
    modified = models.DateTimeField(
        _(u'Modified'),
        auto_now=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_(u'Author')
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_(u'Category')
    )

    objects = models.Manager()
    published_objects = EntryManager()
