from django.db import models


class EntryManager(models.Manager):
    def get_queryset(self):
        return super(EntryManager, self).get_queryset().filter(published=True).order_by(
            '-publication_date')
