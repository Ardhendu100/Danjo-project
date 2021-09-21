from django.db import models
from django.db.models.base import Model

# Create your models here.
from django.db.models.functions import math


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email


class Academic(models.Model):
    content = models.TextField()

class Studentdata(models.Model):

    name = models.CharField(max_length=255)
    id = models.CharField(primary_key='True', max_length=100, default=" ")
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    roll=models.CharField(max_length=20, default=" ")
    Branch=models.CharField(max_length=10, default=" ")
    username=models.CharField(max_length=20, default=" ")
    password=models.CharField(max_length=20)
    parentusername=models.CharField(max_length=20, default=" ")
    profile_pic=models.ImageField(upload_to='home/images', default=" ")
    def __str__(self):
        return self.name

class Teacherdata(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(primary_key='True', max_length=100, default=" ")
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    department = models.CharField(max_length=10, default=" ")
    experience = models.CharField(max_length=20)
    qualification = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    username = models.CharField(max_length=20, default=" ")
    password = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='home/images', default=" ")
    def __str__(self):
        return self.name

class Parentdata(models.Model):
    name = models.CharField(max_length=255)
    guardian_of=models.CharField(max_length=255)
    id = models.CharField(primary_key='True', max_length=100, default=" ")
    roll=models.CharField(max_length=20, default=" ")
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    Address=models.TextField()
    username=models.CharField(max_length=20, default=" ")
    password=models.CharField(max_length=20)
    studentusername=models.CharField(max_length=20, default=" ")
    profile_pic=models.ImageField(upload_to='home/images', default=" ")
    def __str__(self):
        return self.name + '-'+ 'parent of- '+ self.guardian_of

class Examresult(models.Model):
    Name_of_the_Examination = models.CharField(max_length=30)
    Date = models.DateTimeField()
    StudentName = models.CharField(max_length=30)
    username = models.CharField(max_length=20, default=" ")
    StudentRollNo = models.CharField(max_length=30)
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Mathematics = models.IntegerField()
    Computer = models.IntegerField()
    Odia = models.IntegerField()
    English = models.IntegerField()
    TotalMark = models.IntegerField()
    Percentage=models.CharField(max_length=10)
    Grade=models.CharField(max_length=10)
    def __str__(self):
        return self.StudentRollNo



class Dept(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Class(models.Model):

    id = models.CharField(primary_key='True', max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    sem = models.IntegerField()

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        d = Dept.objects.get(name=self.dept)
        return '%s : %d ' % (d.name, self.sem)


class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50, default='X')

    def __str__(self):
        return self.name


class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacherdata, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'class_id', 'teacher'),)

    def __str__(self):
        cl = Class.objects.get(id=self.class_id_id)
        cr = Course.objects.get(id=self.course_id)
        te = Teacherdata.objects.get(id=self.teacher_id)
        return '%s : %s : %s' % (te.name, cr.shortname, cl)


time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)
class AssignTime(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    period = models.CharField(max_length=50, choices=time_slots, default='11:00 - 11:50')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self):
        return  self.day + ' -' + self.period


class AttendanceClass(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default='True')


class BCAAttendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Studentdata, on_delete=models.CASCADE)

    attendanceclass = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE, default=1)
    date = models.DateField(default='2018-10-23')
    status = models.BooleanField(default='True')

    def __str__(self):
        sname = Studentdata.objects.get(name=self.student)
        sbranch=Studentdata.objects.get(name=self.student)
        cname = Course.objects.get(name=self.course)
        return '%s : %s:%s' % (sname.name, cname.shortname,sbranch.Branch)
class BBAAttendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Studentdata, on_delete=models.CASCADE)

    attendanceclass = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE, default=1)
    date = models.DateField(default='2018-10-23')
    status = models.BooleanField(default='True')

    def __str__(self):
        sname = Studentdata.objects.get(name=self.student)
        sbranch=Studentdata.objects.get(name=self.student)
        cname = Course.objects.get(name=self.course)
        return '%s : %s:%s' % (sname.name, cname.shortname,sbranch.Branch)


