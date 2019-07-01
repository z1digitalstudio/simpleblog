from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from simpleblog.models import Entry, Category
from simpleblog.rest_pagination import LimitStartPagination
from simpleblog.serializers import CategorySerializer, EntrySerializer


class CategoryFilter(filters.SearchFilter):
    search_param = "category"

class EntryListView(ListAPIView):
    filter_backends = (CategoryFilter,)
    pagination_class = LimitStartPagination
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    search_fields = ('category__slug', )

class EntryRetrieveView(RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
