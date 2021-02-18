from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):

    """ Categories Admin Definition """

    list_display = ("kind", "name")
