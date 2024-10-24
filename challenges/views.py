from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return   HttpResponse("Masaniamma",status=100)

def february(request):
    return HttpResponse('Hello')

def march(re):
    return HttpResponse('march <a>ht</a>')




