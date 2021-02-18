from django.db import models
from core import models as core_models

# Create your models here.


class Person(core_models.TimeStampedModel):

    """ Person Model Definition """

    KIND_ACT = "actor"
    KIND_DIR = "director"
    KIND_WR = "writer"

    KIND_CHOICES = (
        (KIND_ACT, "Actor"),
        (KIND_DIR, "Director"),
        (KIND_WR, "Writer"),
    )

    name = models.CharField(max_length=30)
    kind = models.CharField(choices=KIND_CHOICES, max_length=8)
    photo = models.ImageField()

    class Meta:
        verbose_name_plural = "people"