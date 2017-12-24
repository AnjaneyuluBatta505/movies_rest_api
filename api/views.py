from decimal import Decimal, InvalidOperation

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer, UserRegisterSerializer, GenreSerializer
from .models import Movie, User, Genre
from .permissions import IsAdmin


class RegisterAPIView(APIView):

    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()
        return Response({'message': 'Registrered successfully'})


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class MoviesViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdmin]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Movie.objects.all().prefetch_related('genre')
        title = self.request.query_params.get('title')
        rating = self.request.query_params.get('rating')
        genre = self.request.query_params.get('genre')
        popularity = self.request.query_params.get('popularity')
        try:
            rating = Decimal(rating)
        except (TypeError, InvalidOperation):
            rating = None
        try:
            popularity = Decimal(popularity)
        except (TypeError, InvalidOperation):
            popularity = None
        if title:
            queryset = queryset.filter(title__icontains=title)
        if rating:
            queryset = queryset.filter(rating__gte=rating)
        if genre:
            queryset = queryset.filter(genre__title__icontains=genre)
        if popularity:
            queryset = queryset.filter(popularity_gte=popularity)
        return queryset
