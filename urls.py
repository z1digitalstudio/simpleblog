from django.conf.urls import patterns, url

from simpleblog.views import IndexView, EntryView, CategoryView, AuthorView

urlpatterns = patterns(
    'simpleblog.views',
    url(
        r'^$',
        IndexView.as_view(),
        name='blog_index'),
    url(
        r'^(?P<slug>[\w-]+)/$',
        EntryView.as_view(),
        name='blog_entry_view'),
    url(
        r'^category/(?P<slug>[\w-]+)/$',
        CategoryView.as_view(),
        name='blog_category_view'),
    url(
        r'^author/(?P<id>[\d]+)/$',
        AuthorView.as_view(),
        name='blog_author_view')
    )
