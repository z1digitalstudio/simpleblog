from django import template

from simpleblog.models import Category, Entry


register = template.Library()


@register.inclusion_tag('simpleblog/categories_list.html')
def categories_list():
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('simpleblog/last_entries.html')
def last_entries():
    entries = Entry.published_objects.all()[:3]
    return {'entries': entries}
