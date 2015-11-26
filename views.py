from django.contrib import auth
from django.views.generic import ListView, DetailView

from simpleblog import settings
from simpleblog.models import Entry, Category
from django.utils.translation import ugettext_lazy as _

PAGINATION_LIMIT = settings.PAGES_NUMBER


class IndexView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    queryset = Entry.published_objects.all()
    template_name = 'simpleblog/index.html'


class EntryView(DetailView):
    model = Entry
    template_name = 'simpleblog/entry.html'


class CategoryView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    template_name = 'simpleblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
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
        author = auth.get_user_model().objects.get(
            id=self.kwargs['id'])
        context['index_kind'] = _(u'Author')
        context['index_title'] = author.first_name + ' ' + author.last_name
        return context

    def get_queryset(self):

        return Entry.published_objects.filter(
            author_id=self.kwargs['id'])
