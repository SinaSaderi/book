from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Author, Publication, Article, Translator, Category

from django.contrib.admin.models import LogEntry


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    LogEntry.objects.all().delete()

@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
