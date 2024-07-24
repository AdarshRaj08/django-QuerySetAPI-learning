from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# QuerySet: A collection of database queries to retrieve objects from your database.

# Create your views here.
def home(request):
    # student_data = Student.objects.all()

    # ################### filter ###############
    # student_data = Student.objects.filter(marks=70)

    # ################### exclude #############
    # student_data = Student.objects.exclude(marks=70)

    # ################### order by ############
    # ascending order 
    # student_data = Student.objects.order_by('marks')

    # descending order
    # student_data = Student.objects.order_by('-marks')

    # randomly
    # student_data = Student.objects.order_by('?')

    # ################## reverse #############
    # student_data = Student.objects.order_by('id').reverse()

    # ################## values ##############
    # # return values in the form of dictionary otherwise return objects
    # student_data = Student.objects.values()

    # # return data on the specific column
    # student_data = Student.objects.values('name','city')
    
    # ################### values_list #############
    # it will return value in the tuple format
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('id','name')
    # student_data = Student.objects.values_list('id','name',named=True)


    # ###################### dates ####################3
    # student_data = Student.objects.dates(field,kind,order='ASC')
    # here field is your column name
    # kind = year,month,week,day
    # student_data = Student.objects.dates('pass_date','day')
    
    # print("-------------------------------")
    # print("REturn : ", student_data)
    # print("------------------------------")


    # ########################### Second Table 'Teacher Started #################################
    # ########################## UNION #######################################
    qs1 = Student.objects.values_list('id','name',named=True)
    qs2 = Teacher.objects.values_list('id','name',named=True)

    # here same no of column should be there in left table selected and right when you performing union
    # student_data = qs2.union(qs1)

    # ############################ AND OR OPERATOR ################################

    # student_data = Student.objects.filter(id=3) & Student.objects.filter(roll=10)
    # student_data = Student.objects.filter(id=3,roll=10)
    # student_data = Student.objects.filter(Q(id=3) & Q(roll=10))

    student_data = Student.objects.filter(id=10) | Student.objects.filter(roll=1)

    # way to see the sql query which is used behind the scene
    print("SQL Query:",student_data.query)
    return render(request,'app/home.html',{'students':student_data})
