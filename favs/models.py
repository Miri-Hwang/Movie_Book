from django.db import models
from core import models as core_models


class FavList(core_models.TimeStampedModel):

    """ FavList Model Definition """

    created_by = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
    books = models.ManyToManyField("books.Book")
    movies = models.ManyToManyField("movies.Movie")

    class Meta:
        verbose_name_plural = "Fav Lists"