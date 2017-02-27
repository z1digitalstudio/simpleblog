from django.contrib import auth
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404
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
        context['facebook_language'] = settings.FACEBOOK_LANGUAGE
        context['facebook_posts_number'] = settings.FACEBOOK_POSTS_NUMBER
        context['facebook_admins'] = settings.FACEBOOK_ADMINS
        context['meta_site_name'] = settings.META_SITE_NAME
        context['absolute_pictures_url'] = settings.ABSOLUTE_PICTURES_URL
        context['fb_app_id'] = settings.FACEBOOK_APP_ID
        return context


class CategoryView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    template_name = 'simpleblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context = set_default_metadata(context)
        category = get_object_or_404(
            Category,
            slug=self.kwargs['slug'])
        context['meta_title'] = category.seo_title
        context['meta_description'] = category.seo_description
        context['index_type'] = _(u'Category')
        context['is_category'] = True
        context['index_title'] = category.name
        return context

    def get_queryset(self):
        return Entry.published_objects.filter(
            category__slug=self.kwargs['slug']
        )


class AuthorView(ListView):
    context_object_name = 'entry_list'
    model = Entry
    paginate_by = PAGINATION_LIMIT
    template_name = 'simpleblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        context = set_default_metadata(context)
        author = get_object_or_404(
            auth.get_user_model(),
            id=self.kwargs['id'])
        context['index_type'] = _(u'Author')
        try:
            context['index_title'] = author.get_full_name()
        except AttributeError:
            context['index_title'] = unicode(author)
        return context

    def get_queryset(self):

        return Entry.published_objects.filter(
            author_id=self.kwargs['id'])
