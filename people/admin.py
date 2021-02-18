from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Person)
class PeopleAdmin(admin.ModelAdmin):

    """ People Admin Definition """

    list_display = ["name", "kind"]
