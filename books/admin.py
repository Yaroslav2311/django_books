from django.contrib import admin

from .models import Author, Book, Publisher, Store


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'publisher', 'pubdate']
    list_filter = ['price', 'rating', 'authors', 'pubdate']
    search_fields = ['name', 'authors']
    date_hierarchy = 'pubdate'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'custom_attr']

    def custom_attr(self, obj):
        return obj.books.count()
    custom_attr.short_description = 'books count'


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Store, StoreAdmin)
