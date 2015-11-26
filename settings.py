from django.conf import settings

PAGES_NUMBER = getattr(settings, 'SIMPLEBLOG_PAGINATION_LIMIT', None)

if PAGES_NUMBER is None:
    PAGES_NUMBER = 10


LAST_ENTRIES = getattr(settings, 'SIMPLEBLOG_LAST_ENTRIES_NUMBER', None)

if LAST_ENTRIES is None:
    LAST_ENTRIES = 3

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', None)

if USER_MODEL is None:
    USER_MODEL = 'auth.User'

TOKEN_CATEGORY = getattr(settings, 'SIMPLEBLOG_URL_TOKEN_CATEGORY', None)

if TOKEN_CATEGORY is None:
    TOKEN_CATEGORY = 'category'

TOKEN_AUTHOR = getattr(settings, 'SIMPLEBLOG_URL_TOKEN_AUTHOR', None)

if TOKEN_AUTHOR is None:
    TOKEN_AUTHOR = 'author'
