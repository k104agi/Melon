from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # User 클래스를 정의함
    # Installed_apps에 members application 추가
    # Auth_user_model 정의 (AppName.ModelClassName)
    # 모든 application들의 migrations 폴더 내의 migration 파일 전부 삭제
    # 이후 makemigrations -> migrate
    # 데이터베이스에 member_user 테이블 생성됐는지 확인
    pass