from django.contrib import admin

from simpleblog.models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
    model = Category

admin.site.register(Category, CategoryAdmin)


class EntryAdmin(admin.ModelAdmin):
    model = Entry

admin.site.register(Entry, EntryAdmin)
