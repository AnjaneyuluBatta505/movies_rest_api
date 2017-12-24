from rest_framework import serializers
from api.models import Movie, User, Genre


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password'
        )


class GenreSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
      model = Genre
      fields = ('id', 'title',)



class MovieSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='title',
        queryset=Genre.objects.all() 
    )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'rating', 'genre', 'popularity'
        )
