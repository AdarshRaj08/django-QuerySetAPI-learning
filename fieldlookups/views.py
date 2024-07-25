from django.shortcuts import render
from .models import Student2
from datetime import date,time
from django.db.models import Avg,Sum,Min,Max,Count
from django.db.models import Q
# Create your views here.


def field(request):
    # student_data = Student2.objects.all()

    ###########################
    # case sensitive
    # student_data = Student2.objects.filter(name__exact='prince')
    # it consider case insensitive
    # student_data = Student2.objects.filter(name__iexact='prInce')
    
    # ##############################
    # it will find any name contain 'in'
    # case sensitive
    # student_data = Student2.objects.filter(name__contains='in')
    # case insensitive
    # student_data = Student2.objects.filter(name__icontains='iN')

    # ################################
    # student_data = Student2.objects.filter(id__in=[1,2,5])
    # student_data = Student2.objects.filter(marks__in=[32,70])
    # marks greater than
    # student_data = Student2.objects.filter(marks_gt=60)
    # greater than equal to 
    # student_data = Student2.objects.filter(marks_gte=60)
    # less than 
    # student_data = Student2.objects.filter(marks_lt=60)
    # less than equal to 
    # student_data = Student2.objects.filter(marks_lte=60)
    # startwith 
    # student_data = Student2.objects.filter(name_startswith='p')
    # caseinsensitive
    # student_data = Student2.objects.filter(name_istartswith='p')
    # endswith
    # student_data = Student2.objects.filter(name_endwith='p')
    # student_data = Student2.objects.filter(name_iendwith='p')
    # range data
    # student_data = Student2.objects.filter(passdate__range=('2024-01-24','2024-09-02'))
    # student_data = Student2.objects.filter(passdate__year=2019)
    # student_data = Student2.objects.filter(passdate__year__gte=2019)
    # student_data = Student2.objects.filter(passdate__month=4)
    # student_data = Student2.objects.filter(passdate__month__gte=4)
    # student_data = Student2.objects.filter(passdate__day=4)
    # student_data = Student2.objects.filter(passdate__day__gt=4)
    # student_data = Student2.objects.filter(passdate__week=23)
    # student_data = Student2.objects.filter(passdate__week__gt=23)
    # week_day - let's say 5 week day is firday then it catch out every frodau
    # student_data = Student2.objects.filter(passdate__week__day=5)
    # student_data = Student2.objects.filter(passdate__week__day__gt=5)
    # quarter
    # student_data = Student2.objects.filter(passdate__quarter=2)

    ########################################### time
    # after 7:55 
    # this work on 24-hour format
    # student_data = Student2.objects.filter(admdatetime__time__gt=time(7,55))
    # value give from 0 to 23
    # student_data = Student2.objects.filter(admdatetime__hour__gt=7)
    # value give from 0 to 59
    # student_data = Student2.objects.filter(admdatetime__minute__gt=45)
    # student_data = Student2.objects.filter(admdatetime__second__gt=45)

    # roll_isnull=False all data will come where null in roll no
    # student_data = Student2.objects.filter(roll_isnull=False)




    # #################### Aggregate Function ###################################

    # student_data = Student2.objects.all()
    # average = student_data.aggregate(Avg('marks'))
    # print(average)     



    # ################## Q-objects ###############################3333
    # student_data = Student2.objects.filter(Q(id=4) & Q(roll=23))
    # student_data = Student2.objects.filter(Q(id=4) | Q(roll=23))
    # student_data = Student2.objects.filter(~Q(id=4))





    # #################### limiting queryset ###############################
    student_data = Student2.objects.all()[:2]
    # student_data = Student2.objects.all()[:12:2]





    # print("------------------------------------------")
    # print("Return:",student_data)
    # print()
    # print("SQL Query: ",student_data.query)

    return render(request,'fieldlookups/field.html',{'students':student_data})

