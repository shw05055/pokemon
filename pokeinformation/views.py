from django.shortcuts import render

# Create your views here.

#--------------------edit--------------------
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 저의 포트폴리오 사이트에 오신것을 환영합니다.")
