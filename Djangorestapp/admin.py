from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','EmpName','Emprole','EmpSal']
admin.site.register(Employee,EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','rollno','marks','age']
admin.site.register(Student,StudentAdmin)

#cricket model..
class CricketerAdmin(admin.ModelAdmin):
    list_display=['id','name','role','jersyno','favshort']
admin.site.register(Cricketer,CricketerAdmin)
