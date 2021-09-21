

from django.shortcuts import render,redirect
from django.http import HttpResponse

from home.models import Contact, Academic ,Studentdata, Examresult, BCAAttendance , BBAAttendance
from.models import Application

from django.contrib import messages

# Create your views here.
def studenthome(request):
    return render(request, 'student/home.html')

def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        # now we have to create a contact object where we can store all the data into our databse , then save the object
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'student/contact.html')


def academic(request):
    post = Academic.objects.all()

    context = {'post': post}

    return render(request,'student/academic.html', context)
def about(request):
    return render(request,'student/about.html')

def studentdashboard(request):
    post=Studentdata.objects.filter(username__icontains=request.user)
    context = {'post': post}
    return render(request, 'student/dashboard.html', context)


def application(request):
    if request.method == "POST":
        name = request.POST['name']
        details = request.POST['details']
        subject = request.POST['subject']
        content = request.POST['content']

        if len(name) < 2 or len(details)<3 or len(subject)<3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")

        # now we have to create a contact object where we can store all the data into our databse , then save the object
        else:
            application = Application(name=name, details=details,subject=subject ,content=content)
            application.save()
            messages.success(request, "Your Application has been successfully sent")

    return  render(request, 'student/application.html')

def result(request):
    post = Examresult.objects.filter(username__icontains=request.user)
    context = {'post': post}
    return render(request, 'student/result.html', context)

def bcaattendance(request):

    bcapresent = BCAAttendance.objects.all()

    context={'bcapresent': bcapresent}
    return  render(request, 'student/attendance.html', context)

def bbaattendance(request):
    bbapresent = BBAAttendance.objects.all()

    context = {'bbapresent': bbapresent}
    return render(request, 'student/attendance.html', context)
