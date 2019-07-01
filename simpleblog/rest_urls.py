from django.conf.urls import url


from simpleblog.rest_views import (
    EntryListView, EntryRetrieveView, CategoryListView
)


urlpatterns = [
    url(
        r'entry/$',
        EntryListView.as_view(),
        name="entry_list"
    ),
    url(
        r'entry/(?P<slug>[\w-]+)/$',
        EntryRetrieveView.as_view(),
        name="entry_retrieve"
    ),
    url(
        r'entry/(?P<id>[\d]+)/$',
        EntryRetrieveView.as_view(),
        name="entry_retrieve"
    ),
    url(
        r'category/$',
        CategoryListView.as_view(),
        name="category_list"
    )
]