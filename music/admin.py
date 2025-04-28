from django.contrib import admin
from .models import UserType, User, Genre, Artist, Album, Song, Playlist, SongRequest, Listen, Favorites, PlaylistSong

# Create a custom AdminSite class
class MyAdminSite(admin.AdminSite):
    final_catch_all_view = False  # Disable the default catch-all view

# Create an instance of the custom admin site
admin_site = MyAdminSite(name='myadmin')

# Register your models with the custom admin site
admin_site.register(UserType)
admin_site.register(User)
admin_site.register(Genre)
admin_site.register(Artist)
admin_site.register(Album)
admin_site.register(Song)
admin_site.register(Playlist)
admin_site.register(SongRequest)
admin_site.register(Listen)
admin_site.register(Favorites)
admin_site.register(PlaylistSong)
