from django.contrib import admin

from .models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'release_year')
    search_fields = ('title',)
