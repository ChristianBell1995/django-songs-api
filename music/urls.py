from django.urls import path
from .views import ListSongsView, RetrieveSongView, CreateSongView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path("songs/<int:pk>", RetrieveSongView.as_view(), name="retrieve-song"),
    path("songs/<str:title>/<str:artist>", CreateSongView.as_view(), name="create-song")
]
