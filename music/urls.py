from django.urls import path
from . import views

# urlpatterns = [
#     # path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('signup/', views.signup_view, name='signup'),
#     path('signup2/', views.signup_view, name='signup2'),
#     path('login/', views.login_view, name='login'),
#     path('login2/', views.login_view, name='login2'),
#     # path('play/', views.song_list, name='song_list'),
#     path('', views.song_list, name='song_list'),
#     path('', views.index, name='index'),
#     path('song/<int:song_index>/', views.song_detail, name='song_detail'),
#     path("play_song/", views.play_song, name="play_song"),
#     path('search/', views.search, name='search'),
#     path('add-to-favorites/<int:song_id>/', views.add_to_favorites, name='add_to_favorites'),
#     path('remove-from-favorites/<int:song_id>/', views.remove_from_favorites, name='remove_from_favorites'),
#     path('play-song/<str:song_title>/', views.play_song, name='play_song'),
#     path('favorites/', views.favorites, name='favorites'),
# ]
import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a file handler and a stream handler
file_handler = logging.FileHandler('app.log')
stream_handler = logging.StreamHandler()

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

urlpatterns = [
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('signup2/', views.signup_view, name='signup2'),
    path('login/', views.login_view, name='login'),
    path('login2/', views.login_view, name='login2'),
    # path('play/', views.song_list, name='song_list'),
    path('', views.song_list, name='song_list'),
   
    path('', views.index, name='index'),
    path('song/<int:song_index>/', views.song_detail, name='song_detail'),
    path("play_song/", views.play_song, name="play_song"),
    path('search/', views.search, name='search'),
    path('add-to-favorites/<int:song_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('my_music/', views.my_music, name='my_music'),
    path('remove-from-favorites/<int:song_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('play-song/<str:song_title>/', views.play_song, name='play_song'),
    path('my_artists/', views.show_artists, name='artists'),
    path('get-artist-songs/<int:artist_id>/', views.get_artist_songs, name='get_artist_songs'),
    path('my_albums/', views.show_album, name='album'),
    path('get-album-songs/<int:album_id>/', views.get_album_songs,name ='get_album_songs'),
    path('my_favorites/', views.favorites, name='favorites'),
    path('top-songs/', views.top_songs, name='top_songs'),
    path('increment-stream/<int:song_id>/', views.increment_stream, name='increment_stream'),
    path('profile/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('request-song/', views.request_song, name='request_song'),

    path('view-song-requests/', views.admin_view_song_requests, name='admin_view_song_requests'),
    path('upload-song/<int:id>/', views.admin_upload_song, name='admin_upload_song'),
    path('reject-request/<int:id>/', views.reject_song_request, name='reject_song_request'),

    path('profile/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/dashboard/songs/', views.view_songs, name='view_songs'),
    path('profile/dashboard/artists/', views.view_artists, name='view_artists'),
    path('profile/dashboard/albums/', views.view_albums, name='view_albums'),
    path('profile/dashboard/genres/', views.view_genres, name='view_genres'),

    path('profile/dashboard/songs/<int:song_id>/', views.song_detail, name='song_list_detail'),
    path('profile/dashboard/songs/edit/<int:song_id>/', views.edit_song, name='edit_song'),
    path('profile/dashboard/songs/delete/<int:song_id>/', views.delete_song, name='delete_song'),
    path('song/increment-stream/<int:song_id>/', views.increment_stream, name='increment_stream'),
    
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/follow/<int:artist_id>/', views.follow_artist, name='follow_artist'),
    path('artists/unfollow/<int:artist_id>/', views.unfollow_artist, name='unfollow_artist'),
    path('artists/followed/', views.followed_artists, name='followed_artists'),
]

# Log the URL patterns
logger.info('URL patterns loaded')