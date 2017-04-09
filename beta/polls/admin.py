from django.contrib import admin

# Register your models here.

from .models import Staff,Person,Contact,Address,Student,Parent,FundRequest,RemReqest,ConReqest

admin.site.register(Staff)
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Student)
admin.site.register(FundRequest)
admin.site.register(RemReqest)
admin.site.register(ConReqest)
admin.site.register(Parent)