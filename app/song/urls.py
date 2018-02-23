from django.urls import path
from . import views

app_name = 'song'
urlpatterns = [
    #song_list view가
    #/song/에서 출력되도록 path 설정
    path('', views.song_list, name='song-list'),
    #song/search/로 들어왔을 때 설정
    path('search/', views.song_search, name='song-search'),
    path('search/melon/',
         views.song_search_from_melon,
         name='song-search-from-melon'),
    path('search/melon/add/',
         views.song_add_from_melon,
         name='song-add-from-melon'),
]