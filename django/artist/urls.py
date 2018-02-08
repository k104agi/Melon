from django.urls import path
from . import views

app_name = 'artist'
urlpatterns = [
    #artist_list view가
    #/artist/에서 출력되도록 path 설정
    path('', views.artist_list, name='artist-list'),
]