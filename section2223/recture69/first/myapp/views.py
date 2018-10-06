from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    """ / トップ """
    context = {
        'name':'Hiroaki'
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    """ /about アバウト """
    return render(request, 'myapp/about.html')

def info(request):
    """ /info インフォページ """
    return render(request, 'myapp/info.html')