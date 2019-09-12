from django.conf.urls import url, include

from simpleblog import settings
from simpleblog.views import IndexView, EntryView, CategoryView, AuthorView

urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(),
        name='blog_index'),
    url(
        r'^(?P<slug>[\w-]+)/$',
        EntryView.as_view(),
        name='blog_entry_view'),
    url(
        r'^' + settings.TOKEN_CATEGORY + '/(?P<slug>[\w-]+)/$',
        CategoryView.as_view(),
        name='blog_category_view'),
    url(
        r'^' + settings.TOKEN_AUTHOR + '/(?P<id>[\d]+)/$',
        AuthorView.as_view(),
        name='blog_author_view'),
    url(
        r'^' + settings.TOKEN_AUTHOR + '/(?P<id>[^/]+)/$',
        AuthorView.as_view(),
        name='blog_author_view'),
    url(
        r'^' + settings.TOKEN_REST + '/',
        include(
            'simpleblog.rest_urls',
            namespace=settings.TOKEN_REST
        )
    )
]
