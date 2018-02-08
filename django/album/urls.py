from django.urls import path
from . import views

app_name = 'album'
urlpatterns = [
    #album_list view가
    #/album/에서 출력되도록 path 설정
    path('', views.album_list, name='album-list')
]