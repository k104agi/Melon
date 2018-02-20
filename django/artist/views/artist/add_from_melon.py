from django.http import HttpResponse

__all__ = ('artist_add_from_melon',)


def artist_add_from_melon(request):
    """
    (1) POST 요청을 받으면 (artist_id를)

    (2) artist_id를 사용해서
    멜론사이트에 들어가 Artist에 들어갈 상세정보 가져오기

    (3) 실제로 저장할 정보 목록
    artist_id
    name
    real_name
    nationality
    birth_date
    constellation
    blood_type
    intro
    위 목록을 채워서 Artist 정보를 생성, DB에 저장하기
    """
    if request.method == 'POST':
        print(request.POST)
        artist_id = request.POST['artist_id']
        return HttpResponse(artist_id)
