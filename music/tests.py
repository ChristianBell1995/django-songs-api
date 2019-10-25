from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Song
from .serializers import SongSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Song.objects.create(title=title, artist=artist)

    def setUp(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        response = self.client.get(reverse("songs-all", kwargs={"version": "v1"}))
        expected = Song.objects.all()
        serialized = SongSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RetrieveSongTest(BaseViewTest):

    def test_retrieve_song(self):
        """
        This test ensures that a song is retrieved by id
        when we make a GET request to the songs/:id endpoint
        """
        response = self.client.get(reverse("retrieve-song", kwargs={"version": "v1", "pk": 1}))
        expected = Song.objects.get(id=1)
        serialized = SongSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateSongTest(BaseViewTest):

    def test_create_song(self):
        """
        This test ensures that a song is created when the correct params
        are given in a POST request to the songs/ endpoint
        """
        self.assertEqual(Song.objects.count(), 4)
        data = {"version": "v1", "title": "Song2", "artist": "blur"}
        response = self.client.post(reverse("create-song", kwargs=data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Song.objects.count(), 5)
        song = Song.objects.all().last()
        self.assertEqual(song.title, data['title'])
        self.assertEqual(song.artist, data['artist'])


