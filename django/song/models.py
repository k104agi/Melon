from django.db import models
from album.models import Album
from artist.models import Artist
from time import strftime

class Song(models.Model):
    album = models.ForeignKey(
        Album,
        verbose_name='앨범',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(
        '곡 제목',
        max_length=100,
    )
    genre = models.CharField(
        '장르',
        max_length=100,
    )
    lyrics = models.TextField(
        '가사',
        blank=True,
    )

    @property
    def artists(self):
        #self.album에 속한 전체 Artist의 Queryset 리턴
        return self.album.artists.all()

    @property
    def release_date(self):
        #self.album의 release_date를 리턴
        return self.album.release_date

    @property
    def formatted_release_date(self):
        #2017.01.15
        # self.release_date가 이런 식으로 출력되도록
        #python strftime 검색
        return self.release_date.strftime('%Y.%m.%d')

#        return self.album.release_date.strftime('%Y.%m.%d')

    def __str__(self):
        # 가수명 - 곡 제목 (앨범명)
        # TWICE(트와이스) - Heart Shaker (Merry & Happy)
        # 휘성, 김태우 - 호호호빵 (호호호빵)
        return '{artists} - {title} ({album})'.format(
            artists=', '.join(self.artists.values_list('name', flat=True)),
            title=self.title,
            album=self.album.title,
        )
