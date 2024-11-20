from django.urls import path
from . import views

urlpatterns = [
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('play/', views.song_list, name='song_list'),
    path("play_song/", views.play_song, name="play_song"),
    path('search/', views.search, name='search'),
]
