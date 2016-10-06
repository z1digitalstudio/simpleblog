import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from simpleblog import settings
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

    def get_absolute_url(self):
        return reverse(
            'blog_category_view', kwargs={'slug': self.slug}
        )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Blog Category')
        verbose_name_plural = _(u'Blog Categories')


class Entry(models.Model):
    title = models.CharField(
        _(u'Title'),
        max_length=200
    )
    slug = models.SlugField(
        _(u'Slug'),
        max_length=100,
        unique=True
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
    publication_date = models.DateTimeField(
        _(u'Publication Date'),
        auto_now_add=True,
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
        settings.USER_MODEL,
        verbose_name=_(u'Author')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_(u'Category')
    )

    objects = models.Manager()
    published_objects = EntryManager()

    def get_absolute_url(self):
        return reverse(
            'blog_entry_view', kwargs={'slug': self.slug}
        )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'Blog Entry')
        verbose_name_plural = _(u'Blog Entries')
        ordering = ['-publication_date']


class EntryImage(models.Model):
    image = models.ImageField(
        _(u'Image'),
        upload_to='blog/images/',
        null=True
    )
    entry = models.ForeignKey(
        Entry,
        related_name="entries",
        verbose_name=_(u'Author')
    )

    class Meta:
        verbose_name = _(u'Entry image')
        verbose_name_plural = _(u'Entry images')


@receiver(pre_save, sender=Entry)
def modify_pub_date(sender, **kwargs):
    instance = kwargs['instance']
    new_pub_state = instance.published
    try:
        old_instance = sender.objects.get(pk=instance.pk)
        old_pub_state = old_instance.published
        if(new_pub_state is True and old_pub_state != new_pub_state):
            instance.publication_date = datetime.datetime.now()
    except(sender.DoesNotExist):
        pass
