from django.contrib import admin

from .models import Navigation

@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent_id')