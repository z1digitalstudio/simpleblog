from django.contrib import admin
from django.forms import ModelForm

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


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
    model = Entry
    prepopulated_fields = {'slug': ('title', )}
    exclude = ['publication_date']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(EntryAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(Entry, EntryAdmin)
