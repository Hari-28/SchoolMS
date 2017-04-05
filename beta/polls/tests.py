from django.test import TestCase
from .models import User,Staff,FeeStruct,Student,Contact, Address,Parent


# Create your tests here.
	


class UserLoginTest(TestCase):
    
	def test_login(self):
		obj2=Staff(salary=10,staffID=3)
		obj2.save()
		obj2=Staff(salary=9,staffID=2)
		obj2.save()
		obj2=Staff(staffID=1)
		obj2.save()
		staff = Staff.objects.get(staffID=1)
		obj=User(userName='test',password='test',staffID=staff)
		obj.save()
		t1 = User.objects.get( userName='test',password='test' )
		t2 = t1.login()
		#self.assertEqual( t2.salary , 10 )
	def test_name(self):
		obj = User(userName='hi',firstName = 'test', middleName = 'my' , lastName = 'name')
		obj.save()
		user = User.objects.get(userName='hi')
		self.assertEqual(user.getName() , 'test my name')
		
	
class FeeTests(TestCase):
    
	def test_tota_fee(self):
		obj2=FeeStruct(acadYear=1,acadFee=100,termFee=100 , vanFee = 100 , classNumber = 2 , startYear = 2010 ,numberTerms=3)	
		obj2.save()	 
		obj2=Student(studentID=9, hasVan=1, classNumber=2, currentYear = 2010 )
		obj2.save()
		f1=FeeStruct.objects.get(acadYear=1)
		s1 = Student.objects.get( studentID = 9 )
		s1.initBalance()
		#self.assertEqual(f1.vanFee , 10)
		self.assertEqual( s1.getBalance() , 2300 )
		

class DetailsCheck(TestCase):
	def test_create_contact(self):
		sta = Staff(salary=2)
		sta.save()
		id=sta.createAddress(address='test',pin = 200, state = 'AP')
		self.assertEqual(id,1)
	
	def test_create_address(self):
		sta = Staff(salary =2) 
		sta.save()
		id = sta.createContact(phoneNumber = 9000000000 , email='rikith.legend@gmail.com')
		self.assertEqual(id,1)
		
	def test_Staff(self):
			obj = Staff(staffID=1,salary=20)
			obj.save()
			obj2 = Staff(salary=20,position = 2)	

			O=Staff.objects.get(staffID=1)
			p=O.registerStaff(obj2,'tests')
			ob = User.objects.get(userName ='tests')
			self.assertEqual(ob.getStaffRole(),2)
		
		
class updateStaff(TestCase) :
		def test_Staff(self):
			obj = Staff(staffID=1,salary=20)
			obj.save()
			obj2 = Staff(salary=20)	

			O=Staff.objects.get(staffID=1)
			p=O.registerStaff(obj2,'tests')
			ob = User.objects.get(userName ='tests')
			self.assertEqual(ob.userName,'tests')
			
			
		def test_headAccountant(self):
			obj = Staff(staffID=1)
			obj.save()
			obj2 = Staff(position=1)
			obj2.save()
			cor = Staff.objects.get(staffID=1)
			cor.setHeadAccountant(2)
			obj = Staff.objects.get(staffID=2)
			self.assertEqual( obj.position , 2 )
			
			
		def test_updateStaff(self):
			acc = Staff( salary=1 )
			acc.save()
			n = Staff(salary =2 )
			
			a = User()
			a.StaffID =1
			a.save()
			
			
			x= User()
			x.firstName = 'test'
			x.middleName = 'for'
			x.lastName = 'name'
			x.dob = '2006-12-19'
			x.sex = 'M'
			acc = Staff.objects.get(staffID=1)
			acc.registerStaff(n,'a')
			
			acc.updateStaff(x,2)
			x = User.objects.get(firstName='test')
			self.assertEqual(x.middleName,'for')
			
			
class AddStudent(TestCase):
	def test_addStudent(self):
		s = Staff(salary = 1 , staffID = 1)
		s.save()
		s = Staff.objects.get(staffID = 1)
		firstName = 'a'
		middleName = 'b'
		lastName = 'c'
		sex = 'M'
		dob = '2006-12-19'
		hasVan = 1
		classNumber = 2
		currentYear = 2017
		st= s.addStudent(firstName,middleName,lastName,sex,dob,classNumber,hasVan,currentYear)
		self.assertEqual(1,st)
	def test_create_contact(self):
		sta = Staff(salary=2)
		sta.save()
		id=sta.createAddress(address='test',pin = 200, state = 'AP')
		self.assertEqual(id,1)
	
	
	def test_create_address(self):
		sta = Staff(salary =2) 
		sta.save()
		id = sta.createContact(phoneNumber = 9000000000 , email='rikith.legend@gmail.com')
		self.assertEqual(id,1)
	
	
	
	def test_addParent(self):
		s = Staff(salary = 1 , staffID = 1)
		s.save()
		sta = Staff(salary=2)
		sta.save()
		aid=sta.createAddress(address='test',pin = 200, state = 'AP')
		cid = sta.createContact(phoneNumber = 9000000000 , email='rikith.legend@gmail.com')
		cid = Contact.objects.get(cID = cid)
		aid = Address.objects.get(addrID = aid)
		s = Staff.objects.get(staffID = 1)
		firstName = 'a'
		middleName = 'b'
		lastName = 'c'
		relation = 'father'
		
		student = Student()
		student.save()
		student = Student.objects.get(studentID=1)
		s.addParent(firstName,middleName,lastName,relation,student,aid,cid)
		a=Parent.objects.get(relation='father')
		#elf.assertEqual(a.relation , 'father')
		