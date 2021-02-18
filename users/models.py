from django.contrib.auth.models import AbstractUser
from django.db import models
from categories import models as categories_model

# Create your models here.
class User(AbstractUser):
    """ Custom User Model """

    PREFERENCES_BOOKS = "books"
    PREFERENCES_MOVIES = "movies"

    PREFERENCES_CHOICES = (
        (PREFERENCES_BOOKS, "Books"),
        (PREFERENCES_MOVIES, "Movies"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_ENGLISH, "English"),
    )

    bio = models.TextField(blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    preferences = models.CharField(
        choices=PREFERENCES_CHOICES, max_length=6, blank=True
    )
    favorite_book_genre = models.ManyToManyField(
        categories_model.Categories, related_name="book_article_set"
    )
    favorite_movie_genre = models.ManyToManyField(
        categories_model.Categories, related_name="movie_article_set"
    )
