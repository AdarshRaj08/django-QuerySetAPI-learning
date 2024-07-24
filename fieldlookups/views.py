from django.shortcuts import render
from .models import Student2
# Create your views here.


def field(request):
    student_data = Student2.objects.all()
    print("Return:",student_data)
    print()
    print("SQL Query: ",student_data.query)

    return render(request,'fieldlookups/field.html',{'students':student_data})

