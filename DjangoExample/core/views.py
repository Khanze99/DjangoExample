from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


def get_view(request):
    a = 1/0
    return HttpResponse("{'code': 200}")