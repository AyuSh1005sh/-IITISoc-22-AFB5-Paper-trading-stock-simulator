from email import message
import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request): 

    if request.method == "POST":
        username = request.POST['username']
        Fname = request.POST['fname']
        Lname = request.POST['Lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name= Fname
        myuser.last_name= Lname

        myuser.save()

        message.success(request,"your account is successfully created.")

        return redirect('signin')
   
    


    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")

def signout(request):
   pass
def support (request):
    return HttpResponse ("Helpline Number - *********** , Email Id - PaperTrade2022@gmail.com")


