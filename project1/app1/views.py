from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        date=request.POST['date']
        num=request.POST['num']
        gender=request.POST['gender']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            return HttpResponse("Password is not matching")
        myusercontact=Contact(fname=fname,lname=lname,date=date,num=num,gender=gender,email=email,pass1=pass1)
        myusercontact.save()
        messages.warning(request,"RESPONSE HAS BEEN RECORDED")
        return redirect('/')
    return render(request,'index.html')