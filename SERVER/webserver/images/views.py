from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Images
from .serializers import ImageSerializer

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image

import datetime
import os


@csrf_exempt
def init(request):
    template = loader.get_template("index.html")
    queryset = Images.objects.all()
    queryset = queryset.order_by("-created")[:8]
    # index.html의 css가 이미지 8개 기준으로 작동하므로 데이터를 가져올때 최신 순으로 8개 가져온다.
    for query in queryset:
        query.caption = query.caption[-29:]
        # /Users/Han/programming/restfulapi/images/static/media/{}.jpg 경로에서 media 부터 시작하기 위함으로 슬라이싱
        # 서버에서는 디렉토리는 달라지겠지만 media가 -29번 부터 시작하는건 동일하기에 위와같이 슬라이싱
    context = {
        "images": queryset,
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def image_send(request):
    if request.method == "GET":
        queryset = Images.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        # return HttpResponse(data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        # img_model = Images()
        try:
            # 여기서 file을 튜플 형태로 client가 보낸 그대로 받아옮.
            file = request.FILES.popitem()
            file = file[1][0]
            binary_file = file.file
            img = Image.open(binary_file)
            # filePath = path.abspath("../webserver/upload_images") + "/test{}.jpg"
            num = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            abspath = os.path.abspath("./images/static/media/test{}.jpg".format(num))
            print(abspath)
            img.save(
                abspath,
                "JPEG",
            )
            serializer = ImageSerializer(data={"caption": abspath, "created": ""})
            if serializer.is_valid():
                print("db 저장 시작")
                serializer.save()
                print("db 저장 성공")
            else:
                print("db 저장 실패")
            return HttpResponse("file received")
        except:
            print("No Post")
            return HttpResponse("No Post")
