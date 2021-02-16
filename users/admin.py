from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Adin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preferences",
                    "language",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                )
            },
        ),
    )

    list_filter = (
        "preferences",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
    )
