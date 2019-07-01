from rest_framework.generics import ListAPIView, RetrieveAPIView

from simpleblog.models import Entry, Category
from simpleblog.rest_filters import SearchCategoryFilter
from simpleblog.rest_pagination import LimitStartPagination
from simpleblog.serializers import CategorySerializer, EntrySerializer


class EntryListView(ListAPIView):
    filter_backends = (SearchCategoryFilter, )
    pagination_class = LimitStartPagination
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryRetrieveView(RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
