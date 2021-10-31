from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

#Login Page
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            now = timezone.now()
            messages.success(request, ('You have been logged in!'))
            return redirect('fileshareapp:Home')
        else:
            messages.success(request, ('Error logging in - Try Again...'))
            return redirect('authentication:Login')
    elif request.user.is_authenticated:   
        return redirect('fileshareapp:Home')
    else:
        return render(request, 'authentication/login.html', {})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('authentication:Login')

def register_user(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            #Check if the user already exists in database
            if User.objects.filter(username=username).exists():
                messages.success(request, ('Username already exists'))
                return redirect('authentication:Register')
            
            elif User.objects.filter(email=email).exists():
                messages.success(request, ('The email Id has already been taken!'))
                return redirect('authentication:Register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, ('Account has been created successfully'))
                return redirect('fileshareapp:Home')
        else:
            messages.success(request, ('Incorrect password!'))
            return redirect('authentication:Register')
    else:
        return render(request, 'authentication/register.html', {})
