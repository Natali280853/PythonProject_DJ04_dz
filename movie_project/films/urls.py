from django.urls import path
# from .views import add_film, list_films
from . import views

urlpatterns = [
    path('add/', views.add_film, name='add_film'),
    path('list/', views.list_films, name='list_films'),
    path('', views.list_films, name='list_films'),
]
