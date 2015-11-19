from django.views.generic import ListView, DetailView
from simpleblog.models import Entry, Category


class IndexView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    queryset = Entry.published_objects.all()
    template_name = 'simpleblog/index.html'


class EntryView(DetailView):
    model = Entry


class CategoryView(ListView):
    model = Entry
    context_object_name = 'entry_list'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(self.kwargs['category'])

    def get_queryset(self):
        return Entry.published_objects.filter(
            category=self.context['category']
        )


class AuthorView(ListView):
    model = Entry
    context_object_name = 'entry_list'

    # def get_context_data(self, **kwargs):
    #     context = super(CategoryView, self).get_context_data(**kwargs)
    def get_queryset(self):
        return Entry.published_objects.filter(
            author=self.context['author']
        )
