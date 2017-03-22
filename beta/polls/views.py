from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    context = {}
    return render(request,'polls/login.html',context)

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username='hari', password='pass')
    if user is not None:
        login(request, user)
        context11 = {}
        return render(request, 'polls/correspondent.html', context11)
    else:
        HttpResponse("Invalid login")

def detail(request):
    return HttpResponse("<h2>Album_id :")

def cor(request):
    context0={}
    return render(request, 'polls/correspondent.html', context0)


def reg(request):
    context={}
    return render(request, 'polls/registar.html', context)

def hreg(request):
    context={}
    html = 'polls/c_addstudent.html'
    HttpResponse(html)
    return render(request,'polls/headregistar.html',context)

def caddstud(request):
    context={}
    return render(request,'polls/c_addstudent.html',context)

def caddreg(request):
    context={}
    return render(request,'polls/c_addregistar.html',context)

def caddstaff(request):
    context={}
    return render(request,'polls/c_addstaff.html',context)

def creq(request):
    context45={}
    return render(request,'polls/c_request.html',context45)