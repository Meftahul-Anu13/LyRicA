from django.urls import path
from . import views

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
    path('my_music/', views.my_music, name='my'),
    path('remove-from-favorites/<int:song_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('play-song/<str:song_title>/', views.play_song, name='play_song'),
]
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
    path('artists/', views.show_artists, name='artists'),
    path('get-artist-songs/<int:artist_id>/', views.get_artist_songs, name='get_artist_songs'),
]

# Log the URL patterns
logger.info('URL patterns loaded')