from django.urls import path
from . import views
from rest_framework.authtoken import views as rest_auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', views.MoviesViewSet, base_name='movies')
router.register(r'genre', views.GenreViewSet, base_name='genre')


urlpatterns = [
    path('login/', rest_auth_views.obtain_auth_token, name='login'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
] + router.urls