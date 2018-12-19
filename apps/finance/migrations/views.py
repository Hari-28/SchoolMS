from django.http import HttpResponse
from django.shortcuts import render
from .models import User,Staff,FeeStruct,Student,Contact, Address
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    #all_albums = Album.objects.all()
    context = {}
    return render(request,'polls/login.html',context)

def my_view(request):
    if request.method == 'POST':
        username = request.POST.get('username11')
        password = request.POST.get('password11')
        try:
		    user = User.objects.get(userName=username , password = password)
		    role = user.getStaffRole()
			
		    if role == 1: #is accountant 
			   context346 = {};
			   return render(request, 'polls/correspondent.html', context346)
		    elif role == 3: #correspondent
			   context346 = {};
			   return render(request, 'polls/correspondent.html', context346)
		    elif role == 2: #HEad 
			   context346 = {};
			   return render(request, 'polls/correspondent.html', context346)
        except ObjectDoesNotExist:
            return HttpResponse("User is not iiitg")

    else:
        return HttpResponse("Invalid method declared.")


def detail(request, album_id):
    return HttpResponse("<h2>Album_id :" + str(album_id) )

def side(request, side_id):
    context110 = {}
    return render(request, 'polls/correspondent.html/'+str(side_id), context110)


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

def caddfac(request):
    context1234={}
    return render(request,'polls/c_addfaculty.html',context1234)

def caddreg(request):
    context={}
    return render(request,'polls/c_addregistar.html',context)

def caddstaff(request):
    context={}
    return render(request,'polls/c_addstaff.html',context)

def creq(request):
    context45={}
    return render(request,'polls/c_request.html',context45)


def capp(request):
    context46={}
    return render(request,'polls/c_approval.html',context46)