from django.contrib import admin
from Practiceapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
      list_display=['id','eid','ename','esal']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)

