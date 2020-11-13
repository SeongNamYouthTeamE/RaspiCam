# RaspiCam
A Project with raspberry pi camera, web and iOS

# 20201021
- 클라우드 서비스(네이버클라우드)에서 대여한 서버에 해당 origin remote의 issue3 브랜치 받아오기
- Ubuntu 16.04 위에 Python 개발 환경 설정 및 Django 환경 구축
- Python: 3.9
- Django: 2.2.6
- 기타 설치: djangorestframework, markdown, django-filter
- 포트포워딩 통해서 외부접속 확인 완료

# 20201023
- images 앱 생성
- model 생성
- serializer 생성
- views에 이미지 수신하는 함수 생성
- url에 맵핑

# 20201031
- images에 html 파일을 넣을 templates 폴더 생성(index.html 생성 후 static 렌더링 설정)
- images에 css, js, images 등 리소스를 넣을 static 폴더 생성(추후 유환님이 넣을 수 있게)
- settings.py 에 static 관련 사전 설정
- url에 맵핑
- SERVER라는 상위폴더 생성후 서버 관련 파일 전체 이동

# 20201107 ~ 20201112
- Dockerfile 생성 및 작성
- docker-compost 생성 및 작성
- alpine linux 이미지 위에 python, django 등 환경 설정 완료
- Pillow를 제대로 받아오지 못하는 오류 발생
- importError: Error loading shared libraries libjpeg.so.8:
- 다양한 자료를 참고하여 패키지들을 add 해주었는데 타 리눅스 image 기반으로 작성되어 있어서 그런지 non-zero code 에러 연달아 발생
- https://github.com/python-pillow/Pillow/issues/1763
- https://stackoverflow.com/questions/56407216/django-does-not-find-pillow-though-installed
- 위 링크 들을 참고
- https://pkgs.alpinelinux.org/packages 공식 문서에서 패키지 검색하며 찾음
- docker image를 rebuild 하는 법을 몰라서 docker rmi -f 로 이미지 삭제 후 진행 반복..
- 성공