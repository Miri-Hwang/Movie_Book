from django.contrib.auth.models import AbstractUser
from django.db import models

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

    BGENRE_POEM = "poems"
    BGENRE_NOVEL = "novels"
    BGENRE_ESSAYS = "essays"

    BGENRE_CHOICES = (
        (BGENRE_POEM, "Poems"),
        (BGENRE_NOVEL, "Novels"),
        (BGENRE_ESSAYS, "Essays"),
    )

    MGENRE_HORROR = "horror"
    MGENRE_ROMANCE = "romance"
    MGENRE_COMEDY = "comedy"

    MGENRE_CHOICES = (
        (MGENRE_HORROR, "Horror"),
        (MGENRE_COMEDY, "Comedy"),
        (MGENRE_ROMANCE, "Romance"),
    )

    bio = models.TextField(blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    preferences = models.CharField(
        choices=PREFERENCES_CHOICES, max_length=6, blank=True
    )
    favorite_book_genre = models.CharField(
        choices=BGENRE_CHOICES, max_length=20, blank=True
    )
    favorite_movie_genre = models.CharField(
        choices=MGENRE_CHOICES, max_length=20, blank=True
    )
