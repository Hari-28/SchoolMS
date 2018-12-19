from django.contrib import admin

# Register your models here.

from .models import Staff,User,Contact,Address,Student

admin.site.register(Staff)
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Student)