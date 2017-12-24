import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from api.models import Movie, Genre


class Command(BaseCommand):
    help = 'Load movie data from json file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(
            settings.BASE_DIR, "api", "management", "commands", "data.json"
        )
        with open(file_path, 'r') as f:
            data = json.loads(f.read()).get('data')
            for movie in data:
                genre_list = []
                for genre in movie.get('genre'):
                    genre, _ = Genre.objects.get_or_create(title=genre)
                    genre_list.append(genre)
                try:
                    movie, _ = Movie.objects.get_or_create(
                        title=movie.get('name'),
                        director=movie.get('director'),
                        rating=movie.get('rating'),
                        popularity=movie.get('popularity'),
                    )
                    movie.genre.add(*genre_list)
                except:
                    pass
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
