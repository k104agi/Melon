from django.db import models

from artist.models import Artist


class Album(models.Model):
    title = models.CharField(
        '앨범명',
        max_length=100,
    )
    img_cover = models.ImageField(
        '커버 이미지',
        upload_to='album',
        blank=True,
    )
    artists = models.ManyToManyField(
        Artist,
        verbose_name='아티스트 목록',
    )
    release_date = models.DateField()

    @property
    def genre(self):
        # 장르는 가지고 있는 노래에서 가져오기
        return ', '.join(self.song_set.values_list('genre', flat=True).distinct())

    def __str__(self):
        # 호호호빵 [휘성 (Realslow), 김태우]
        # Merry & Happy [TWICE (트와이스)]
        # 이렇게 나오도록 작성할 것
        # 전체쿼리: self.artists.all()
        # values_list 사용
        return '{title} [{artists}]'.format(
            title=self.title,
            artists=', '.join(self.artists.values_list('name', flat=True))
        )
    # 위 함수를 넣음으로써 album object(1), (2)로 표시되던게
    # 앨범명[가수명]으로 나오게 되었음
