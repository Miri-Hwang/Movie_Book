from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MoviesAdmin(admin.ModelAdmin):

    """ Movies Admin Definition """

    list_display = ["title", "year", "rating", "director"]
