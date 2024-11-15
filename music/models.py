# music/models.py

from django.db import models

class UserType(models.Model):
    user_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_type_name

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)
    streams = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()  # Duration in seconds
    file_url = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist_count = models.IntegerField(default=1)
    released_year = models.IntegerField()
    released_month = models.IntegerField()
    released_day = models.IntegerField()
    streams = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SongRequest(models.Model):
    user = models.ForeignKey(User, related_name='requests', on_delete=models.CASCADE)
    admin = models.ForeignKey(User, related_name='admin_requests', on_delete=models.CASCADE)
    song_title = models.CharField(max_length=255)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.song_title} by {self.user.name}"

class Listen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    played_at = models.DateTimeField()
    status = models.CharField(max_length=100)
    play_mode = models.CharField(max_length=100)

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
