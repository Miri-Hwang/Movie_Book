from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.FavList)
class FavsAdmin(admin.ModelAdmin):

    """ Favs Admin Definition """

    pass
