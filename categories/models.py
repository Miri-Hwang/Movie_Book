from django.db import models
from core import models as core_models


class Categories(core_models.TimeStampedModel):

    """ Categories Model Definition """

    KIND_BOOK = "book"
    KIND_MV = "movie"
    KIND_BOTH = "both"

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MV, "Movie"),
        (KIND_BOTH, "Both"),
    )
    name = models.CharField(max_length=30)
    kind = models.CharField(choices=KIND_CHOICES, max_length=5)

    class Meta:
        verbose_name_plural = "Categories"