from rest_framework import filters


class SearchCategoryFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('category'):
            return ('category__name', 'category__slug')
        return super(SearchCategoryFilter, self).get_search_fields(view, request)
