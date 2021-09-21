from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact, Academic

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout

from student.models import Application


def home(request):
    return render(request, 'home/home.html')

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
    return render(request, 'home/contact.html')


def academic(request):
    post = Academic.objects.all()

    context = {'post': post}

    return render(request,'home/academic.html', context)

def stulogin(request):
    return render(request,'home/stulogin.html')
def studentLogin(request):
    if request.method == "POST":
        # Get the post parameters
        stuusername = request.POST['stuusername']
        stupassword = request.POST['stupassword']

        user = authenticate(username=stuusername, password=stupassword)
        if user is not None:
            if stupassword[:3] == "stu":
                login(request, user)
                messages.success(request, f"Successfully Logged In {stuusername}")
                return redirect("studenthome")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

    

def teachLogin(request):
    return render(request,'home/teachLogin.html')
def teacherLogin(request):
    if request.method == "POST":
        # Get the post parameters
        teachusername = request.POST['teachusername']
        teachpassword = request.POST['teachpassword']

        user = authenticate(username=teachusername, password=teachpassword)
        if user is not None:
            if teachpassword[:3] == "tea":
                login(request, user)


                messages.success(request, f"Successfully Logged In {teachusername}")
                return redirect("teacherhome")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def parlogin(request):
    return render(request,'home/parentlogin.html')

def parentlogin(request):
    if request.method == "POST":
        # Get the post parameters
        parusername = request.POST['parusername']
        parpassword = request.POST['parpassword']

        user = authenticate(username=parusername, password=parpassword)
        if user is not None:
            if parpassword[:3] == "par":
                login(request, user)


                messages.success(request, f"Successfully Logged In {parusername}")
                return redirect("parenthome")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def application(request):
    if request.method == "POST":
        name = request.POST['name']
        details = request.POST['details']
        subject = request.POST['subject']
        content = request.POST['content']

        if len(name) < 2 or len(details) < 3 or len(subject)<3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")


        # now we have to create a contact object where we can store all the data into our database , then save the object
        else:
            application = Application(name=name, details=details,subject=subject ,content=content)
            application.save()
            messages.success(request, "Your Application has been successfully sent")

    post = Application.objects.filter(status__icontains=request.user)
    return  render(request, 'home/application.html')

def bca(request):
    return render(request,'home/bca.html')
def bba(request):
    return render(request,'home/bba.html')
def mba(request):
    return render(request,'home/mba.html')
def pgdm(request):
    return render(request,'home/pgdm.html')
def mata(request):
    return render(request,'home/mata.html')

def about(request):
    return render(request,'home/about.html')