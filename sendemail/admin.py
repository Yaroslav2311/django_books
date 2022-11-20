from django.contrib import admin

from .models import Authors, Phrases


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class PhraseAdmin(admin.ModelAdmin):
    list_display = ['phrase', 'author']
    search_fields = ['phrase', 'authors']


admin.site.register(Authors, AuthorAdmin)
admin.site.register(Phrases, PhraseAdmin)
