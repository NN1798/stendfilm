from django.contrib import admin

from .models import (
    Composition, Company, Genre, Country, Award, Rating, Comment
)


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'type', 'release_year',
        'get_average_rating', 'get_count_comment',
    )
    list_display_links = ('id', 'title')
    list_filter = ('title', 'release_year', 'type')
    search_fields = ('title',)

    def get_average_rating(self, obj):
        return obj.average_rating()
    get_average_rating.short_description = 'Средний рейтинг'


    def get_count_comment(self, obj):
        return obj.count_comment()
    get_count_comment.short_description = 'Кол-во комментариев'


admin.site.register(Company)


admin.site.register(Genre)


admin.site.register(Country)


admin.site.register(Award)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('composition', 'score', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'composition')
