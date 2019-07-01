from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


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

TOKEN_REST = getattr(settings, 'SIMPLEBLOG_URL_TOKEN_REST', None)

if TOKEN_REST is None:
    TOKEN_REST = 'rest'

TWITTER_ACCOUNT = getattr(settings, 'SIMPLEBLOG_TWITTER_ACCOUNT', None)

if TWITTER_ACCOUNT is None:
    raise ImproperlyConfigured('SIMPLEBLOG_TWITTER_ACCOUNT is not defined in settings.')

FACEBOOK_SITE_NAME = getattr(settings, 'SIMPLEBLOG_FACEBOOK_SITE_NAME', None)

if FACEBOOK_SITE_NAME is None:
    raise ImproperlyConfigured('SIMPLEBLOG_FACEBOOK_SITE_NAME is not defined in settings.')

FACEBOOK_LANGUAGE = getattr(settings, 'SIMPLEBLOG_FACEBOOK_LANGUAGE', None)

if FACEBOOK_LANGUAGE is None:
    FACEBOOK_LANGUAGE = "en_EN"

FACEBOOK_POSTS_NUMBER = getattr(settings, 'SIMPLEBLOG_FACEBOOK_POSTS_NUMBER', None)

if FACEBOOK_POSTS_NUMBER is None:
    FACEBOOK_POSTS_NUMBER = 5

FACEBOOK_ADMINS = getattr(settings, 'SIMPLEBLOG_FACEBOOK_ADMINS', None)

if FACEBOOK_ADMINS is None:
    FACEBOOK_ADMINS = []

FACEBOOK_APP_ID = getattr(settings, 'SIMPLEBLOG_FACEBOOK_APP_ID', None)

if FACEBOOK_APP_ID is None:
        FACEBOOK_APP_ID = ""

ABSOLUTE_PICTURES_URL = getattr(settings, 'SIMPLEBLOG_ABSOLUTE_PICTURES_URL', None)

if ABSOLUTE_PICTURES_URL is None:
        ABSOLUTE_PICTURES_URL = False

META_TITLE = getattr(settings, 'SIMPLEBLOG_DEFAULT_META_TITLE', None)

if META_TITLE is None:
    raise ImproperlyConfigured('SIMPLEBLOG_DEFAULT_META_TITLE is not defined in settings.')


META_DESCRIPTION = getattr(settings, 'SIMPLEBLOG_DEFAULT_META_DESCRIPTION', None)

if META_DESCRIPTION is None:
    raise ImproperlyConfigured('SIMPLEBLOG_DEFAULT_META_DESCRIPTION is not defined in settings.')


META_AUTHOR = getattr(settings, 'SIMPLEBLOG_DEFAULT_META_AUTHOR', None)

if META_AUTHOR is None:
    raise ImproperlyConfigured('SIMPLEBLOG_DEFAULT_META_AUTHOR is not defined in settings.')


META_SITE_NAME = getattr(settings, 'SIMPLEBLOG_DEFAULT_META_SITE_NAME', None)

if META_SITE_NAME is None:
    raise ImproperlyConfigured('SIMPLEBLOG_DEFAULT_META_SITE_NAME is not defined in settings.')
