from django.contrib import admin

# Register your models here.

from .models import Staff,User

admin.site.register(Staff)
admin.site.register(User)