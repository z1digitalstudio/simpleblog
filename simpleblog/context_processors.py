from simpleblog import settings
from simpleblog.models import Category, Entry


def simpleblog_context(request):
    entries = Entry.published_objects.all()[:settings.LAST_ENTRIES]
    categories = Category.objects.all()
    return {'categories': categories,
            'entries': entries
            }
