# music/admin.py

from django.contrib import admin
from .models import UserType, User, Genre, Artist, Album, Song, Playlist, SongRequest, Listen, Favorites, PlaylistSong

admin.site.register(UserType)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(SongRequest)
admin.site.register(Listen)
admin.site.register(Favorites)
admin.site.register(PlaylistSong)
