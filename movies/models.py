from django.db import models
from core import models as core_models


class Movie(core_models.TimeStampedModel):

    """ Movie Model Definition """

    Rating_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    title = models.CharField(max_length=40)
    year = models.IntegerField()
    category = models.ManyToManyField("categories.Categories")
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField(choices=Rating_CHOICES)
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="directors_set"
    )
    cast = models.ManyToManyField("people.Person", related_name="casts_set")

    def __str__(self):
        return f"{self.title} by {self.director}"