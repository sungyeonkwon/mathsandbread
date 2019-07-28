from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    redirect('register') 
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                    )
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
                    # user.save()
                    # messages.success(request, 'You are now registered and can log in')
                    # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            redirect('register')
        print('submitted, registed')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')