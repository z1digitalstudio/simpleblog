from django.contrib import auth
from django.contrib.sites.models import Site
from django.views.generic import ListView, DetailView

from simpleblog import settings
from simpleblog.models import Entry, Category
from django.utils.translation import ugettext_lazy as _

PAGINATION_LIMIT = settings.PAGES_NUMBER


def set_default_metadata(context):
    context['meta_title'] = settings.META_TITLE
    context['meta_description'] = settings.META_DESCRIPTION
    context['meta_author'] = settings.META_AUTHOR
    context['meta_site_name'] = settings.META_SITE_NAME
    return context


class IndexView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    queryset = Entry.published_objects.all()
    template_name = 'simpleblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context = set_default_metadata(context)
        return context


class EntryView(DetailView):
    model = Entry
    template_name = 'simpleblog/entry.html'

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        context['twitter_account'] = settings.TWITTER_ACCOUNT
        context['facebook_site_name'] = settings.FACEBOOK_SITE_NAME
        context['site_name'] = settings.META_SITE_NAME
        return context


class CategoryView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    template_name = 'simpleblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context = set_default_metadata(context)
        context['index_kind'] = _(u'Category')
        context['index_title'] = Category.objects.get(
            slug=self.kwargs['slug']).name
        return context

    def get_queryset(self):
        return Entry.published_objects.filter(
            category=Category.objects.get(
                slug=self.kwargs['slug'])
        )


class AuthorView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    template_name = 'simpleblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        context = set_default_metadata(context)
        author = auth.get_user_model().objects.get(
            id=self.kwargs['id'])
        context['index_kind'] = _(u'Author')
        context['index_title'] = author.first_name + ' ' + author.last_name
        return context

    def get_queryset(self):

        return Entry.published_objects.filter(
            author_id=self.kwargs['id'])
