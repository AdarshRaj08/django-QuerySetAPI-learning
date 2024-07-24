from django.contrib import admin
from .models import Student2

# Register your models here.
@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','marks','passdate','admdatetime']
