from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from . models import Images
from . serializers import ImageSerializer
from PIL import Image
from os import path

# Create your views here.

num = 1


@csrf_exempt
def init(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


@csrf_exempt
def image_send(request):
    global num
    if request.method == 'GET':
        queryset = Images.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        # return HttpResponse(data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # img_model = Images()
        try:
            # 여기서 file을 튜플 형태로 client가 보낸 그대로 받아옮.
            file = request.FILES.popitem()
            file = file[1][0]
            binary_file = file.file
            img = Image.open(binary_file)
            filePath = path.abspath("./images/static/images/thumbs") + "/test{}.jpg"
            img.save(filePath.format(num), 'JPEG')

            # serializer = ImageSerializer(data={'image': img, 'created':'2020-01-01'})
            # if serializer.is_valid():
            #     print("db 저장 시작")
            #     serializer.save()
            #     print("db 저장 성공")

            num += 1
            return HttpResponse("file received")
        except:
            print("No Post")
            return HttpResponse("No Post")
