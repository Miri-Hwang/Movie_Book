from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    Rating_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.IntegerField(choices=Rating_CHOICES)

    def __str__(self):
        return f"{self.created_by} - {self.rating}"