#  jango 학습 정리 (1~4일차)

# 01. jango 기초
- Django란? : Python 기반의 웹 프레임워크
- MTV 패턴 (Model - Template - View)
- Django 설치 및 프로젝트 생성
- `python manage.py runserver` 명령어로 서버 실행
- 앱 생성: `python manage.py startapp 앱이름`

---

# 02. jango Model
- 모델이란? : 데이터베이스 구조를 정의하는 클래스
- `models.Model`을 상속받아 사용
- 필드 종류:
  - `CharField(max_length=100)`
  - `IntegerField()`, `DateTimeField()`, `BooleanField()` 등
- 마이그레이션
  - `python manage.py makemigrations`
  - `python manage.py migrate`

---

# 03. jango Admin
- 관리자 페이지 자동 생성: `python manage.py createsuperuser`
- `admin.py`에 모델 등록: `admin.site.register(모델명)`
- 관리자 페이지에서 데이터 CRUD 가능
- 커스터마이징 예: `list_display`, `search_fields`, `list_filter`

---

# 04. jango ORM 
- ORM(Object-Relational Mapping) = 파이썬 코드로 DB 조작
- 주요 명령어:
  - 생성: `Model.objects.create(필드=값)`
  - 조회: `Model.objects.get(id=1)`, `Model.objects.filter(조건)`
  - 수정: `객체.필드 = 값; 객체.save()`
  - 삭제: `객체.delete()`
- `python manage.py shell`로 실습 가능
