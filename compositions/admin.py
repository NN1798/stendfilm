from django.contrib import admin

from .models import Composition, Company, Genre, Country, Award


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'release_year')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'release_year', 'type')
    search_fields = ('title',)


admin.site.register(Company)


admin.site.register(Genre)


admin.site.register(Country)


admin.site.register(Award)
