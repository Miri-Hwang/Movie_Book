from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewsAdmin(admin.ModelAdmin):

    """ Reviews Admin Definition """

    pass
