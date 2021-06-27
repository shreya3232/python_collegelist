from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import College
from .serializers import Collegeserializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def college_list(request):
    if request.method == 'GET':
        colleges = College.objects.all()
        serializer = Collegeserializer(colleges, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Collegeserializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
