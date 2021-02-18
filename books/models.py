from django.db import models
from core import models as core_models
from people import models as people_models


class Book(core_models.TimeStampedModel):

    """ Book Model Definition """

    Rating_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    title = models.CharField(max_length=40)
    year = models.IntegerField()
    category = models.ManyToManyField("categories.Categories")
    cover_image = models.ImageField()
    rating = models.IntegerField(choices=Rating_CHOICES)
    writer = models.ManyToManyField("people.Person")
