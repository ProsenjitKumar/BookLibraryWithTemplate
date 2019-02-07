from django.contrib import admin
from .models import (
    Category,
    Author,
    Book,
    BookInstance,
    Currency,
    Language,
    Tag,
    Editor,
    Translator,
    Publisher,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name_of_the_book', 'isbn', 'published', 'publisher']
    search_fields = ['name_of_the_book', 'isbn']
    prepopulated_fields = {'slug': ('name_of_the_book',)}


admin.site.register(Book, BookAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['publisher']
    search_fields = ['publisher']


admin.site.register(Publisher, PublisherAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'imprint', 'due_back']


admin.site.register(BookInstance, BookInstanceAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name',]
    search_fields = ['full_name',]


admin.site.register(Author, AuthorAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['currency']
    search_fields = ['currency']
    prepopulated_fields = {'slug': ('currency',)}


admin.site.register(Currency, CurrencyAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language']
    search_fields = ['language']


admin.site.register(Language, LanguageAdmin)


class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['translator']
    search_fields = ['translator']


admin.site.register(Translator, TranslatorAdmin)


class EditorAdmin(admin.ModelAdmin):
    list_display = ['editor']
    search_fields = ['editor']


admin.site.register(Editor, EditorAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Tag, TagAdmin)
