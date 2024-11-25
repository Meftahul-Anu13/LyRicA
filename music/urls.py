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
]
