from django.conf.urls import patterns, url

from simpleblog.views import IndexView

urlpatterns = patterns(
    'simpleblog.views',
    url(
        r'^$',
        IndexView.as_view(),
        name='blog_index')
    )
