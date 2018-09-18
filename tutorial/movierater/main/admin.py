from django.contrib import admin
from .models import Movie, ExtraInfo, Review, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_display = ('name', 'description', 'year', 'released')
    list_filter = ('year', 'released')
    search_fields = ('name',)


admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Actor)
