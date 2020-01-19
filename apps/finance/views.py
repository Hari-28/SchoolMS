from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import authenticate, login
from  django.core.exceptions import ObjectDoesNotExist
from .models import Person,Staff,FeeStruct,Student,Contact, Address,Parent
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    return render(request,'polls/login.html')

def login(request):
     if request.method == 'POST':
        username = request.POST.get('username11')
        password = request.POST.get('password11')
        # try:
            # user = Person.objects.get(userName=username, password = password)
            # role = user.getStaffRole()

            # if role == 'A': #is accountant 
            #     context346 = {}
            #     return render(request, 'polls/correspondent.html', context346)
            # elif role == 'C': #correspondent
            #     context346 = {}
            #     return render(request, 'polls/correspondent.html', context346)
            # elif role == 'H': #HEad 
        context346 = {}
        return render(request, 'polls/correspondent.html', context346)
        # except ObjectDoesNotExist:
            # return HttpResponse("Person is not iiitg")
     else:
        return render(request, 'polls/correspondent.html',)

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
            #return HttpResponse("Person is div : 1    ;" + str(filename) + str(remark))
            return render(request, 'polls/c_request.html',)
        elif div == s3:
            name = request.POST.get('name')
            id = request.POST.get('id')
            salary = request.POST.get('salary')
            amount = request.POST.get('amount')
            remarks = request.POST.get('remark')
            #return render(request, 'polls/c_request.html',)
            return HttpResponse("Person is div : 2    ;" + str(name)+ str(id) + str(salary)+ str(amount) + str(remarks))
        elif div == s5:
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            roll = request.POST.get('roll')
            amount = request.POST.get('amount')
            remarks = request.POST.get('remark')
            return render(request, 'polls/c_request.html',)
            #return HttpResponse("Person is div : 2    ;" + str(name)+ str(sclass) + str(roll)+ str(amount) + str(remarks))
        elif div == s6:
            sclass = request.POST.get('class')
            section = request.POST.get('section')
            filename = request.POST.get('filename')
            remark = request.POST.get('remark')
            return HttpResponse("Person is div : 1    ;" + str(sclass) + str(section) + str(filename) + str(remark))
            #return render(request, 'polls/c_request.html',)
        elif div == s7:
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            return HttpResponse("Person is div : 1    ;" + str(sclass) + str(name) )
            #return render(request, 'polls/c_request.html',)
        else:
            return HttpResponse("Div is not equal to 1 but is equal to " + str(request.POST.get('div')))
    else:
        return render(request, 'polls/correspondent.html',)

def caddstud(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        mname = request.POST.get('middlename')
        lname = request.POST.get('lastname')
        dob = '2017-03-29'#request.POST.get('dob')
        gender = request.POST.get('gender')
        gfname = request.POST.get('gfirstname')
        gmname = request.POST.get('gmiddlename')
        glname = request.POST.get('glastname')
        email = request.POST.get('email')
        relation = request.POST.get('relation')
        mobile = request.POST.get('mobile')
        address = request.POST.get('add')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        sclass = request.POST.get('class')
        transport = request.POST.get('transport')
        context={}
        admin = Staff.objects.get(staffID=1)
        sid= admin.addStudent(fname,mname,lname,gender,dob,sclass,transport,2017)
        cID = admin.createContact( email , mobile)
        cID = Contact.objects.get(cID=cID)
        aID = admin.createAddress(address,pin,state)
        aID = Address.objects.get(addrID=aID)
        student = Student.objects.get(studentID=sid)
        admin.addParent(gfname,gmname,glname,relation,student,aID,cID)
        #p= Person(firstName=fname,middleName=mname,lastName=lname,sex=gender,dob=dob,studentID=sid)
        
        return render(request, 'polls/c_addstudent.html', context)
    else:
        return render(request, 'polls/c_addstudent.html',)

def caddfac(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        context={  }
        return render(request, 'polls/c_addfaculty.html', context)
    else:
        context={"a" : request.COOKIES['id']}
        return render(request, 'polls/c_addfaculty.html', context)

def caddreg(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		address = request.POST.get('add')
		
		
		
		context={}
		return render(request, 'polls/c_addregistar.html', context)
		#return HttpResponse("Person is not iiitg" + str(name) + str(email) + str(address))
	else:
		return render(request, 'polls/c_addregistar.html',)


		
'''
this is redundant accountant is a staff d nw
'''
def caddstaff(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('add')
        middleName = 'a'
        lastName = 'b'
        dob ='2017-03-29'
        sex = 'M'
        joinDate='2017-03-29'
        position = 'Accountant'
        salary = 1000
        admin.registerStaff()
        
        
        
        
        context={}
        return render(request, 'polls/c_addstaff.html',context )
        #return HttpResponse("Person is not iiitg" + str(name) + str(email) + str(address))
    else:
        return render(request, 'polls/c_addstaff.html',)

def creq(request):
    admin = Staff.objects.get(staffID=1)
    if request.method == 'POST':
        div = request.POST.get('div')
        s1="funds"
        s2="concession"
        s3="3"
        if div == s1:
            amount = request.POST.get('amount') 
            reason = request.POST.get('reason')
            x = admin.addFunReq(amount,reason) 
            #x is the id of req in all cases
            #return HttpResponse("Person is div : 1    ;" + str(amount) + str(reason))
            return render(request, 'polls/c_request.html',)
        elif div == s2:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            studentID = request.POST.get('sid')
            x = admin.addConReq(studentID,amount,reason)
            #x = admin.addRemReq(studentID,amount,reason)
            sclass = request.POST.get('class')
            return render(request, 'polls/c_request.html',)
            #return HttpResponse("Person is div : 2    ;" + str(amount) + str(reason)+ str(sclass) + str(name))
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
            return HttpResponse("Person is div : 1    ;" + str(amount) + str(reason))
            #return render(request, 'polls/c_approval.html',)
        elif div == s2:
            amount = request.POST.get('amount')
            reason = request.POST.get('reason')
            name = request.POST.get('name')
            sclass = request.POST.get('class')
            #return render(request, 'polls/c_approval.html',)
            return HttpResponse("Person is div : 2    ;" + str(amount) + str(reason)+ str(sclass) + str(name))
        elif div ==s3:
            return HttpResponse("Div is not equal to 1 but is equal to " + str(request.POST.get('div')))
    else:
        return render(request, 'polls/c_approval.html',)



def csfee(request):
    if request.method == 'POST':
        bl = request.POST.get('bl')
        tl = request.POST.get('tl')
        sl = request.POST.get('sl')
        bu = request.POST.get('bu')
        tu = request.POST.get('tu')
        su = request.POST.get('su')
        b1 = request.POST.get('b1');t1 = request.POST.get('t1');s1 = request.POST.get('s1')
        b2 = request.POST.get('b2');t2 = request.POST.get('t2');s2 = request.POST.get('s2')
        b3 = request.POST.get('b3');t3 = request.POST.get('t3');s3 = request.POST.get('s3')
        b4 = request.POST.get('b4');t4 = request.POST.get('t4');s4 = request.POST.get('s4')
        b5 = request.POST.get('b5');t5 = request.POST.get('t5');s5 = request.POST.get('s5')
        b6 = request.POST.get('b6');t6 = request.POST.get('t6');s6 = request.POST.get('s6')
        b7 = request.POST.get('b7');t7 = request.POST.get('t7');s7 = request.POST.get('s7')
        b8 = request.POST.get('b8');t8 = request.POST.get('t8');s8 = request.POST.get('s8')
        b9 = request.POST.get('b9');t9 = request.POST.get('t9');s9 = request.POST.get('s9')
        b10 = request.POST.get('b10');t10 = request.POST.get('t10');s10 = request.POST.get('s10')
        return HttpResponse("Person is div : 1    ;" + str(sl) + str(bl) + str(tl) + str(bu))
    else:
        return render(request, 'polls/c_setfee.html', )





def reg(request):
    context={}
    return render(request, 'polls/registar.html', context)

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