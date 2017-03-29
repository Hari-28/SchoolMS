from django.db import models

class User(models.Model):

   gender = ( ( 'M' , 'Male' ) , ( 'F' , 'Female' ) )
   firstName = models.CharField(max_length = 50)
   middleName = models.CharField(max_length = 50)
   lastName = models.CharField(max_length = 50)
   userName = models.CharField(max_length=50, primary_key=True	)
   password = models.CharField(max_length = 50)
   dob = models.DateField(null=True)
   sex = models.CharField( max_length = 1,choices = gender )
   staffID = models.ForeignKey('Staff',null = True )
   studentID = models.ForeignKey('Student',null=True)
   def login(self):
		user=User.objects.get(userName=self.userName, password= self.password)
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
		user = User(staffID=obj,userName=username, password ='password')
		user.save()
		return username
		
   def setHeadAccountant(self,ID):
		x= Staff.objects.get(staffID=ID)
		x.position=2
		x.save()
		return 1
		
		
   def updateStaff(self,user,ID):
		s = Staff.objects.get(staffID=ID)
		x = User.objects.get(staffID=s)
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
   acadYear = models.IntegerField( null= True)
   vanFee = models.IntegerField( default=0)
   termFee = models.IntegerField( default=0 )
   acadFee = models.IntegerField( default=0 )
   startYear = models.IntegerField( null= True ) 
   classNumber = models.IntegerField( null=True ) 
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
	
