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
    print("return :", student_data)

    # way to see the sql query which is used behind the scene
    # print("SQL Query:",student_data.query)
    return render(request,'app/home.html',{'students':student_data})



# #################################### Method that don't return new QuerySets ##########################################

def second(request):

    # ################### Retriving a single Object ###########################3
    
    # get() - it returns a single object . no result match it will raise DoesNotExist exception.
    # student_data = Student.objects.get(id=1)


    # #################################
    # first() - it return the first object matched by the queryset or None if there is no matching object
    #         - if no order defined then queryset is automatically ordered by the primary key.

    # last()  - opposite of first
    # latest() - latest according to the date
    # earliest()

    # student_data = Student.objects.first()

    # here we first do order by marks
    # student_data = Student.objects.order_by("marks").first()

    # student_data = Student.objects.earliest('pass_date')

    #############################
    # exists() - it returns True if the QuerySet contain any results,False if not.
    #          - this run on query set not on the single object ( see below way to check one object exists or not)

    # student_data = Student.objects.all()
    # print(student_data.exists())

    # for checking one object exists or not
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())


    # ##################################
    # create() - it will create new object and save it

    # student_data = Student.objects.create(name='Sameer',roll=114,
    #                                       city='Bokaro',marks=60,pass_date='2020-5-4')


    # get_or_create() - it will give if the data present if not present then it will create

    # if created then true here in student data the value will be there 
    # student_data,created = Student.objects.get_or_create(name='Anisha',roll=117,
    #                                       city='Bokaro',marks=67,pass_date='2020-8-4')



    ###########################################
    # update() - it apply on queryset not on single objects
    
    # student_data = Student.objects.filter(id=6).update(roll=23,marks=120)
    # print(student_data)           #  It returns the number of rows matched by the query and subsequently updated.

    

    # ############################################
    # bulk_create() - create object in bulk
    # objs = [
    #     Student(name='Atif',roll=118,city='Dhanbad',marks=70,
    #             pass_date='2020-6-12'),
    #     Student(name='aslam',roll=128,city='Mitho',marks=90,
    #             pass_date='2020-8-12'),
    #     Student(name='rustom',roll=198,city='mohammad',marks=78,
    #             pass_date='2022-2-28'),
    # ]

    # student_data = Student.objects.bulk_create(objs)

    # #####################################
    # bulk_update() - update in bulk

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city  = 'Dhanbad'
    # student_data = Student.objects.bulk_update(all_student_data,['city'])


    # ##########################################3
    # in_bulk([pks]) 

    # here we accessing more than one [7,5] primarykeys 
    # student_data = Student.objects.in_bulk([7,5])
    # print(student_data[7].name)          # give the attribute name



    # ##############################################
    # delete()
    # student_data = Student.objects.get(pk=6).delete()
    # student_data = Student.objects.filter(marks=70).delete()
    # student_data = Student.objects.all().delete()


    # ##############################################33
    # count() - give count to the data
    student_data = Student.objects.all()
    print(student_data.count())


    print("------------------------------------")
    print("return :", student_data)
    # print()
    # print("SQL Query: ", student_data.query)
    return render(request,'app/hii.html',{'student':student_data})