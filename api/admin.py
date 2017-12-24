from django.contrib import admin
from .models import User, Genre, Movie

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Movie)