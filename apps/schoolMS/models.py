from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    user_name = models.CharField(max_length=50, primary_key=True	)
    password = models.CharField(max_length = 50)
    dob = models.DateField(null=True)
    sex = models.CharField( max_length = 1 ,null=True)
    is_parent = models.IntegerField(default=0)

class Class ( models.Model ):
    classNumber = models.IntegerField(primary_key=True )
    numberSections = models.IntegerField(null = True)
    acadYear = models.IntegerField(null = True)

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

class Subject (models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subjectName = models.CharField(max_length=50)
    lessonPlan = models.CharField( max_length=50 )

class FundRequest(models.Model):
    fund_id = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    reason = models.CharField(max_length=100)
    amount = models.IntegerField()

class ConReqest(models.Model):
    con_id =models.IntegerField(primary_key=True)
    status = models.IntegerField()
    reason = models.CharField(max_length=100)
    amount = models.IntegerField()
    student_id = models.ForeignKey('Student')

class RemReqest(models.Model):
    rem_id = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    reason = models.CharField(max_length=100)
    amount = models.IntegerField()

class FinancialReport(models.Model):
    year = models.IntegerField()
    amount = models.IntegerField()
    reason = models.CharField(max_length=100)
