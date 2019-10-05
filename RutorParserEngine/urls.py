from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_torrent, name='search_torrent'),
]