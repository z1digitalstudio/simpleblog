from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from simpleblog.models import Entry, Category
from simpleblog.rest_pagination import LimitStartPagination
from simpleblog.serializers import (
    CategorySerializer, EntrySerializer, EntryDetailSerializer)


class CategoryFilter(filters.SearchFilter):
    search_param = "category"

class EntryListView(ListAPIView):
    filter_backends = (CategoryFilter,)
    pagination_class = LimitStartPagination
    queryset = Entry.objects.all().order_by('-publication_date')
    serializer_class = EntrySerializer
    search_fields = ('category__slug', )

class EntryRetrieveView(RetrieveAPIView):
    queryset = Entry.objects.all().order_by('-publication_date')
    serializer_class = EntryDetailSerializer


class CategoryListView(ListAPIView):
    pagination_class = LimitStartPagination
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
