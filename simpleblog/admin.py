from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from simpleblog.models import Category, Entry

from redactor.widgets import RedactorEditor


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)


class EntryAdminForm(ModelForm):

    class Meta:
        widgets = {

            'content': RedactorEditor(redactor_settings={
                'formattingTags': ['p', 'blockquote', 'pre', 'h2', 'h3',
                                   'h4', 'h5', 'h6'],
                'buttons': [
                    'formatting', 'bold', 'italic', 'deleted',
                    'unorderedlist', 'orderedlist', 'link', 'html'
                    ]}
                )}


class AuthorFilter(admin.SimpleListFilter):
    title = _('Author')
    parameter_name = 'author__id__exact'

    def lookups(self, request, model_admin):
        author_model = get_user_model()
        authors = author_model.objects.annotate(
            num_entries=Count('entry')).filter(num_entries__gt=0).distinct()
        lookup_list = ()
        for author in authors.all():
            lookup_list = lookup_list + ((author.pk, author),)
        return lookup_list

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(author__pk=self.value())


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
    model = Entry
    prepopulated_fields = {'slug': ('title', )}
    exclude = ['publication_date']
    list_display = ('title', 'category', 'published', 'publication_date')
    search_fields = ['title']
    list_filter = (AuthorFilter, 'category',
                   'publication_date', 'published')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(EntryAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(Entry, EntryAdmin)
