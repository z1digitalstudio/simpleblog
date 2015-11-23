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
                'buttons': [
                    'formatting', 'bold', 'italic', 'deleted',
                    'unorderedlist', 'orderedlist', 'link', 'html'
                ]
            })
        }


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
    model = Entry
    prepopulated_fields = {'slug': ('title', )}
    exclude = ['publication_date']

admin.site.register(Entry, EntryAdmin)
