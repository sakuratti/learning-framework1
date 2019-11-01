from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, id, name):
    result = 'あなたのIDは' + str(id) + '名前は' + name

    return HttpResponse(result)