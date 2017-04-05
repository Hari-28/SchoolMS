from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
from django.contrib.auth import authenticate, login

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums':all_albums,}
    return render(request,'polls/login.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username11')
        password = request.POST.get('password11')
        ss = "iiitg"
        ss1 = "iiitghr"
        ss2  = "iiitgr"
        if username == ss:
            context346 = {"username": username}
            return render(request, 'polls/correspondent.html', context346)
        elif username == ss1:
            return render(request, 'polls/headregistar.html', )
        elif username == ss2:
            return render(request, 'polls/registar.html', )
        else:
            return HttpResponse("User is not iiitg" + str(username))



def cor(request):
    if request.method == 'POST':
        div = request.POST.get('div')
        s1="expenses"
        s3="salary"
        s5="fees"
        s6 = "attend"
        s7 = "grade"
        if div == s1:
            filename = request.POST.get('filename')
            remark = request.POST.get('remark')
            #return HttpResponse("User is div : 1    ;" + str(filename) + str(remark))
            return render(request, 'polls/c_request.html',)
        elif div == s3:
            name = request.POST.get('name')
            id = request.POST.get('id')
            salary = request.POST.get('salary')
            amount = request.POST.get('amount')
            remarks = request.POST.get('remark')
            #return render(request, 'polls/c_request.html',)
            return HttpResponse("User is div : 2    ;" + str(name)+ str(id) + str(salary)+ str(amount) + str(remarks))
        elif div == s5:
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            roll = request.POST.get('roll')
            amount = request.POST.get('amount')
            remarks = request.POST.get('remark')
            return render(request, 'polls/c_request.html',)
            #return HttpResponse("User is div : 2    ;" + str(name)+ str(sclass) + str(roll)+ str(amount) + str(remarks))
        elif div == s6:
            sclass = request.POST.get('class')
            section = request.POST.get('section')
            filename = request.POST.get('filename')
            remark = request.POST.get('remark')
            return HttpResponse("User is div : 1    ;" + str(sclass) + str(section) + str(filename) + str(remark))
            #return render(request, 'polls/c_request.html',)
        elif div == s7:
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            return HttpResponse("User is div : 1    ;" + str(sclass) + str(name) )
            #return render(request, 'polls/c_request.html',)
        else:
            return HttpResponse("Div is not equal to 1 but is equal to " + str(request.POST.get('div')))
    else:
        return render(request, 'polls/correspondent.html',)

def caddstud(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sclass = request.POST.get('class')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/c_addstudent.html', context)
    else:
        return render(request, 'polls/c_addstudent.html',)

def caddfac(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/c_addfaculty.html', context)
        #return HttpResponse("User is not iiitg" + str(name) + str(email) + str(address))
    else:
        return render(request, 'polls/c_addfaculty.html', )

def caddreg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/c_addregistar.html', context)
        #return HttpResponse("User is not iiitg" + str(name) + str(email) + str(address))
    else:
        return render(request, 'polls/c_addregistar.html',)


def caddstaff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/c_addstaff.html',context )
        #return HttpResponse("User is not iiitg" + str(name) + str(email) + str(address))
    else:
        return render(request, 'polls/c_addstaff.html',)

def creq(request):
    if request.method == 'POST':
        div = request.POST.get('div')
        s1="funds"
        s2="concession"
        s3="3"
        if div == s1:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            #return HttpResponse("User is div : 1    ;" + str(amount) + str(reason))
            return render(request, 'polls/c_request.html',)
        elif div == s2:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            return render(request, 'polls/c_request.html',)
            #return HttpResponse("User is div : 2    ;" + str(amount) + str(reason)+ str(sclass) + str(name))
        elif div ==s3:
            return HttpResponse("Div is not equal to 1 but is equal to " + str(request.POST.get('div')))
    else:
        return render(request, 'polls/c_request.html',)

    #context45={}
    #return render(request,'polls/c_request.html',context45)


def capp(request):
    if request.method == 'POST':
        div = request.POST.get('div')
        s1="funds"
        s2="concession"
        s3="3"
        if div == s1:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            return HttpResponse("User is div : 1    ;" + str(amount) + str(reason))
            #return render(request, 'polls/c_approval.html',)
        elif div == s2:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            #return render(request, 'polls/c_approval.html',)
            return HttpResponse("User is div : 2    ;" + str(amount) + str(reason)+ str(sclass) + str(name))
        elif div ==s3:
            return HttpResponse("Div is not equal to 1 but is equal to " + str(request.POST.get('div')))
    else:
        return render(request, 'polls/c_approval.html',)



























####################################################################################


def reg(request):
    context={}
    return render(request, 'polls/registar.html', context)















####################################################################################


def hreg(request):
    context={}
    html = 'polls/c_addstudent.html'
    HttpResponse(html)
    return render(request,'polls/headregistar.html',context)

def haddstud(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sclass = request.POST.get('class')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/h_addstudent.html', context)
    else:
        return render(request, 'polls/h_addstudent.html',)

def haddfac(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/h_addfaculty.html', context)
    else:
        return render(request, 'polls/h_addfaculty.html', )

def haddstaff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        context={}
        return render(request, 'polls/h_addstaff.html',context )
    else:
        return render(request, 'polls/h_addstaff.html',)

def hreq(request):
    if request.method == 'POST':
        div = request.POST.get('div')
        s1="funds"
        s2="concession"
        s3="3"
        if div == s1:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            return render(request, 'polls/h_request.html',)
        elif div == s2:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            return render(request, 'polls/h_request.html',)
        elif div ==s3:
            return HttpResponse("Div is not equal to 1 but is equal to " + str(request.POST.get('div')))
    else:
        return render(request, 'polls/h_request.html',)
