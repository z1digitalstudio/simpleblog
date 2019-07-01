from rest_framework.pagination import LimitOffsetPagination


class LimitStartPagination(LimitOffsetPagination):
    offset_query_parameter = 'start'
