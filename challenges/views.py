from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.


def index(request):
    return   HttpResponse("Masaniamma",status=100)

def february(request):
    return HttpResponse('Hello')

def march(re):
    return HttpResponse('march <a>ht</a>')



def monthly_challenges(request,month):
    text=None
    if month=='january':
        text='Hello janu'
        
    elif month=='february':
        text="february"
        
    elif month=='march':
        text="March"
        
    else:
        return HttpResponseNotFound("This month not supported")
    return HttpResponse(text)
    

