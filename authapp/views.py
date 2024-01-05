from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re   # defined a URL pattern using a regular expressiion re

# Create your views here.
def signup(request):
    flag=0
    if request.method=="POST":			# here if user request == these posts will okay all
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        #print(name,email,password,confirm_password)
        if password != confirm_password:
                messages.warning(request, "Password is not matching")
                return redirect("/auth/signup/")
        if len(password)<=8:
            messages.warning(request,"Password must be at least 8 characters")
            return redirect('/auth/signup/')
        elif not re.search("[a-z]", password):
            flag=-1
        elif not re.search("[A-Z]", password):
            flag=-1
        elif not re.search("[0-9]", password):
            flag=-1
        elif not re.search("[@#%$*!^()-_/]", password):
            flag=-1
        else:
            pass
        if(flag==0):
            try:
                if User.objects.get(username=email):
                    messages.warning(request, "Email is Taken")    # if user used same user and name will send
								   # message 'Email is Taken' 
                    return redirect("/auth/signup/")
                
            except Exception as identifier:
                pass
            user = User.objects.create_user(email, email, password)  # here user name email password if 								     # correct saved
            user.first_name=name
            #user.is_active=True
            user.save()
            messages.success(request,"Signup Success Please login")  # if everything is corrected then will 
								     # message 'Signup Success Please login'
								     # then return to login page
            return redirect('/auth/login/')
        else:
            messages.error(request, "Password is not valid")
            return redirect("/auth/signup/")

    return render(request, "signup.html")




def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get("email")
        userpassword = request.POST.get("pass1")
        myuser = authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect("/")
            
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/auth/login/")

    return render(request, "login.html")



def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return render(request,"login.html")