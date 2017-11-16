from django.shortcuts import render

def index(request):
    name = 'Nikita'
    return render(request, 'index/index.html', locals())







