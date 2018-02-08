from django.urls import path
from . import views

app_name = 'song'
urlpatterns = [
    #song_list view가
    #/song/에서 출력되도록 path 설정
    path('', views.song_list, name='song-list')
]