from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BooksAdmin(admin.ModelAdmin):

    """ Books Admin Definition """

    list_display = ("title", "year", "category", "rating", "writer")
