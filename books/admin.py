from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BooksAdmin(admin.ModelAdmin):

    """ Books Admin Definition """

    pass