from django.db import models

import datetime

class Person(models.Model):

  firstName = models.CharField(max_length = 50)
  middleName = models.CharField(max_length = 50)
  lastName = models.CharField(max_length = 50)
  userName = models.CharField(max_length=50, primary_key=True	)
  password = models.CharField(max_length = 50)
  dob = models.DateField(null=True)
  sex = models.CharField( max_length = 1 ,null=True)
  staffID = models.ForeignKey('Staff',null = True )
  studentID = models.ForeignKey('Student',null=True)
  isParent = models.IntegerField(default=0)
  def login(self):
    user=Person.objects.get(userName=self.userName, password= self.password)
    staff= user.staffID 
    return staff

  def getStaffRole(self):
    return self.staffID.position

  def getName(self):
    return self.firstName+' '+self.middleName+' '+self.	lastName




class Staff(models.Model):
  positions = ( (1,'Accountant') ,  (2,'Head Accountant') , (3, 'Correspondent') )
  staffID = models.IntegerField(primary_key=True)
  salary = models.IntegerField(default = 0,null=True)
  position = models.IntegerField( null = True ,choices = positions )
  salaryToBePaid = models.IntegerField(null = True, default =0 )
  joinDate = models.DateField( null=True )
  cID = models.ForeignKey('Contact',null = True)
  addrID = models.ForeignKey('Address', null = True)

  def registerStaff(self,staff,username):
    x=Staff.objects.filter().count()+1
    obj = Staff(position =staff.position , salary = staff.position , joinDate = staff.joinDate , staffID = x ) 

    ''' cID = staff.cID , addrID = staff.addrID ,'''
    obj.salaryToBePaid=10;
    obj.save()
    obj= Staff.objects.get(staffID=x)
    user = Person(staffID=obj,userName=username, password ='password')
    user.save() 
    return username

  def setHeadAccountant(self,ID):
    x= Staff.objects.get(staffID=ID)
    x.position=2
    x.save()
    return 1

  def updateStaff(self,user,ID):
    s = Staff.objects.get(staffID=ID)
    x = Person.objects.get(staffID=s)
    x.firstName = user.firstName
    x.middleName = user.middleName
    x.lastName = user.lastName
    x.dob = user.dob
    x.sex = user.sex
    x.save()
    return 1

  def createContact(self, email , phoneNumber):
    cID = Contact.objects.filter().count()+1
    c= Contact(cID = cID , email = email , phoneNumber = phoneNumber)
    c.save()
    return cID

  def createAddress(self,address,pin,state):
    addrID = Address.objects.filter().count()+1
    a = Address(addrID = addrID ,address=address , pin = pin , state = state )		
    a.save()
    return addrID


  def addStudent(self,firstName,middleName,lastName,sex,dob,classNumber,hasVan,currentYear):

    s = Student.objects.filter().count()+1
    x = Student(classNumber=classNumber,hasVan=hasVan,currentYear=currentYear,studentID=s)
    x.save()
    id = Student.objects.get(studentID=s)
    ids = Staff.objects.get(staffID=1)
    x = Person(firstName=firstName,middleName=middleName,lastName=lastName,sex=sex,dob=dob,studentID=id,staffID=ids,userName = firstName+lastName+str(datetime.datetime.now()))
    x.save()
    p = Person.objects.get(studentID=id)
    p.firstName
    return s

  def addParent(self,firstName,middleName,lastName,relation,student,aID,cID):
    staffID = Staff.objects.get(staffID=1) 
    u = Person(firstName=firstName,middleName=middleName,lastName=lastName,studentID=student,isParent=1,staffID=staffID,userName = firstName+lastName+str(datetime.datetime.now()))
    u.save()
    p = Parent(relation=relation,addrID=aID,cID=cID,studentID=student)
    p.save() 

  def setContactStaff(self,sid,cid):
    s = Staff.objects.get(staffID=sid)
    cid = Contact.objects.get(cID=cid)
    s.cID = cid
    s.save()

  def setAddressStaff(self,sid,aid):
    s = Staff.objects.get(staffID=sid)
    cid = Address.objects.get(aID=aid)
    s.aID = aid
    s.save()

  def setContactParent(self,sid,cid):
    s = Student.objects.get(studentID=sid)
    pa = Parent.objects.get(studentID=s)

    cid = Contact.objects.get(cID=cid)
    pa.cID = cid
    pa.save()


  def setAddressStaff(self,sid,aid):
    s = Student.objects.get(studentID=sid)
    pa = Parent.objects.get(studentID=s)
    aid = Address.objects.get(aID=aid)
    pa.aID = aid
    pa.save()

  def approveFund(self,fundID):
    f=FundRequest(fundID=fundID)
    f.status=1
    f.save()
    x=FinancialReport(year = datetime.date.today().year , amount = -(x.amount), reason = x.reason)  
    x.save()
    return 1


  def approveRembursment(self,remID):
    f=RemReqest(remID=remID)
    f.status=1
    f.save()
    x=FinancialReport(year = datetime.date.today().year , amount = -(x.amount), reason = x.reason)  
    x.save()
    return 1

  def approveConcession (self,conID):
    f=ConRequest(fundID=fundID)
    f.status=1
    f.student.feesToBePaid -= f.amount*10 
    f.student.save()
    x.save()
    return 1
  def addFunReq(self,amount,reason):
    x=FundRequest.objects.filter().count()+1
    f = FundRequest(fundID=x,amount=amount,reason=reason,status=0)
    f.save()
    return x
  def addRemReq(self,studentID,amount,reason):
    x=RemReqest.objects.filter().count()+1
    try:
      stu = Student.get.objects(studentID=staffID)
      f = RemReqest(remID=x,amount=amount,reason=reason,status=0,studentID = stu)
      f.save()
      return x
    except:
      return -1
  def addConReq(self,studentID,amount,reason):
    try:
      x=ConReqest.objects.filter().count()+1		
      stu = Student.objects.get(studentID=studentID)
      f = ConReqest(conID = x,amount=amount,reason=reason,status=0,studentID=stu)
      f.save()
      return x
    except:
      return -1

  def insertfeeStruct(self):
    a=12


class Contact(models.Model):
  cID = models.IntegerField()
  email = models.EmailField( max_length=100 , null=True)
  phoneNumber = models.IntegerField( )

class Address(models.Model):
  addrID = models.IntegerField( primary_key=True)
  address = models.CharField(max_length = 50 , null = True)
  pin = models.IntegerField(null = True)
  state = models.CharField(max_length = 50 , null = True)

class Parent(models.Model):
  cID = models.ForeignKey('Contact', default=1)
  addrID = models.ForeignKey('Address', default=1)
  relation = models.CharField( max_length = 50, null = True )
  studentID = models.ForeignKey('Student',default=1)

class Student(models.Model):
  studentID  = models.IntegerField( primary_key = True )
  classNumber = models.IntegerField( null = True )
  feesToBePaid = models.IntegerField( null = True )
  hasVan = models.IntegerField(null = True)
  currentYear = models.IntegerField( null=True )
  def initBalance(self):
  #f1= FeeStruct(startYear = self.currentYear , classNumber = self.classNumber )
    f1= FeeStruct.objects.get(startYear = self.currentYear , classNumber = self.classNumber )
    vanFee = f1.total_vanfee() * self.hasVan
    acadFee = f1.total_acadfee()
    termFee = f1.total_termfee()
    self.feesToBePaid = vanFee + acadFee + termFee
    self.save()

  def getBalance(self):
    return self.feesToBePaid

class Class ( models.Model ):
  classNumber = models.IntegerField(primary_key=True )
  numberSections = models.IntegerField(null = True)
  acadYear = models.IntegerField(null = True)
  def makeAcadYear(self,acadYear):
    for i in range(-1,11):
      c = Class(classNumber = i,acadYear = acadYear )
      c.save()



class Section ( models.Model ): 
  classNumber = models.ForeignKey('Class',default=1)
  strength = models.IntegerField( null = True )
  sectionName = models.CharField( max_length=2,null = True )


class FeeStruct ( models.Model ): 
#classList = ( ( -1 , 'LKG' ) , ( 0 , 'UKG' ) , (1,1) , (2,2) , (3,3), (4,4), (5,5),(6,6) , (7,7) , (8,8) , (9,9) (10,10) )

  acadYear = models.IntegerField( primary_key=True)
  vanFee = models.IntegerField( default=0)
  termFee = models.IntegerField( default=0 )
  acadFee = models.IntegerField( default=0 )
  startYear = models.IntegerField( null= True ) 
  classNumber = models.IntegerField( primary_key=True ) 
  numberTerms = models.IntegerField (default=3)
  def total_vanfee(self):
    return self.vanFee * 10
  def total_termfee(self):
    return self.termFee * self.numberTerms
  def total_acadfee(self):
    return self.acadFee * 10;

class Subject (models.Model):
  subjectId = models.IntegerField(primary_key=True)
  subjectName = models.CharField(max_length=50)
  lessonPlan = models.CharField( max_length=50 )

class FundRequest(models.Model):
  fundID = models.IntegerField(primary_key=True)
  status = models.IntegerField()
  reason = models.CharField(max_length=100)
  amount = models.IntegerField()

class ConReqest(models.Model):
  conID =models.IntegerField(primary_key=True)
  status = models.IntegerField()
  reason = models.CharField(max_length=100)
  amount = models.IntegerField()
  studentID = models.ForeignKey('Student')
  def addConReq(studentID,amount,reason):
    x=ConRequest.objects.filter().count()+1		
    stu = Student.get.objects(studentID=staffID)
    f = ConRequest(conID = x,amount=amount,reason=reason,status=0,studentID=stu)
    f.save()
    return x

class RemReqest(models.Model):
  remID = models.IntegerField(primary_key=True)
  status = models.IntegerField()
  reason = models.CharField(max_length=100)
  amount = models.IntegerField()

class FinancialReport(models.Model):
  year = models.IntegerField()
  amount = models.IntegerField()
  reason = models.CharField(max_length=100)
