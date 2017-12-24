from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


ADMIN = 1
USER = 2


ACCESS_LEVEL_CHOICES = (
    (ADMIN, 'Admin'),
    (USER, 'User'),
)

class User(AbstractUser):
    access_level = models.IntegerField(choices=ACCESS_LEVEL_CHOICES, default=USER)


class Genre(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    genre = models.ManyToManyField(Genre)
    popularity = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    director = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
