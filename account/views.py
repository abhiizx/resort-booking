
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def login_view(request):
    if request.method == 'GET':
        return render(request,'account/login.html')
    elif request.method =='POST':
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request,username=uname,password=pswd)
        if uname=='admin' and pswd=='admin':
            return redirect('adm')
        elif user is not None:
            login(request,user)
            return redirect('user_home')
        else:
            return render(request,'account/login.html')
def signup(request):
    if request.method=='GET':
        return render(request,'account/signup.html')
    elif request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        adhar=request.POST['adhar']
        address=request.POST['address']
        email=request.POST['email']
        phnno=request.POST['mobileno']
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        obj1=CustomerDetails(fname=fname,lname=lname,age=age,adhar=adhar,address=address,email=email,phnno=phnno)
        obj2=User(username=uname)
        obj2.set_password(pswd)
        obj2.save()
        obj1.user=obj2
        obj1.save()
        return redirect('login')
def logout_view(request):
	logout(request)
	return redirect('login')




