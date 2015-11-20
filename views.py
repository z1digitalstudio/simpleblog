from django.views.generic import ListView, DetailView
from simpleblog.models import Entry, Category


class IndexView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    queryset = Entry.published_objects.all()
    template_name = 'simpleblog/index.html'


class EntryView(DetailView):
    model = Entry
    template_name = 'simpleblog/entry.html'


class CategoryView(ListView):
    model = Entry
    context_object_name = 'entry_list'
    template_name = 'simpleblog/category.html'

    def get_queryset(self):
        return Entry.published_objects.filter(
            category=Category.objects.get(slug=self.kwargs['slug'])
        )


class AuthorView(ListView):
    model = Entry
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.published_objects.filter(
            author=self.context['author']
        )
