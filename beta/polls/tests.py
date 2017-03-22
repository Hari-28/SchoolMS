from django.test import TestCase
from .models import User,Staff,FeeStruct,Student


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
		
    
		
		