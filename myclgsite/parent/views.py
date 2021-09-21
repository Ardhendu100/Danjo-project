from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from home.models import Contact, Academic,Examresult ,Parentdata
from.models import Application
# Create your views here.
def parenthome(request):
    return render(request, 'parent/home.html')


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
    return render(request, 'parent/contact.html')
def academic(request):
    post = Academic.objects.all()

    context = {'post': post}

    return render(request,'parent/academic.html', context)

def about(request):
    return render(request,'parent/about.html')

def parentdashboard(request):
    post=Parentdata.objects.filter(username__icontains=request.user)
    context = {'post': post}
    return render(request, 'parent/dashboard.html', context)
    
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

    return  render(request, 'parent/application.html')


def result(request):
    data=Parentdata.objects.filter(username__icontains=request.user)
    print(data)
    rollno=data.values('roll')
    print(rollno)
    r=rollno[0]['roll']
    print(r)
  
  
   
    post=Examresult.objects.filter(StudentRollNo=r)
    context = {'post': post}
    


    return render(request, 'parent/result.html', context)

