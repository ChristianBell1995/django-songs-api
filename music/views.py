from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from .models import Song
from .serializers import SongSerializer

# Create your views here.


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class RetrieveSongView(generics.RetrieveAPIView):
    """
    Retrieves a song based on the id
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class CreateSongView(generics.CreateAPIView, CreateModelMixin):
    # """
    # Creates a song with a title and an artist
    # """
    # queryset = Song.objects.all()
    # serializer_class = SongSerializer
