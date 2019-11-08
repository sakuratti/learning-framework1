from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

# Create your views here.
def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'あなたの情報:',
        'form':HelloForm()
    }
    return render(request,'hello/index.html',params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは,nextページです。',
        'goto':'index',
    }
    return render(request,'hello/index.html',params)

def form(request):
    msg = request.POST['msg']
    params = {
    'title':'Hello/Form',
    'msg':'こんにちは'+msg+'さん!',
    }
    if (request.method == 'POST'):
        params['message'] = '名前:'+request.POST['name']+¥
        '<br>メール:'+request.POST['mail']+¥
        '<br>年齢:'+request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', params)