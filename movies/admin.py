from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MoviesAdmin(admin.ModelAdmin):

    """ Movies Admin Definition """

    pass
