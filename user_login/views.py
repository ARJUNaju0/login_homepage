from django.shortcuts import render, redirect
from .models import Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


def home(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    password = request.session.get('password')

    if user_id:
        other_users = Login.objects.exclude(id=user_id)  # show everyone except the logged-in user
        return render(request, 'home.html', {'username': username,'users': other_users,})
        return render(request, 'home.html', {'username': username})
    else:
        return redirect('login')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST.get('confirm_password')
        if password != c_password:
            messages.error(request, "Passwords do not match")
            return redirect('Register')        
        if not Login.objects.filter(username=username).exists():
            hashed_password = make_password(password)
            login_user = Login(username=username, password=hashed_password)
            login_user.save()
            messages.success(request,'User registered successfully. Please login.')
            return redirect("login")
        else:
            return render(request, 'register.html', {'error': 'Username already exists'})
    return render(request, 'register.html' )


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(username=username)
            if check_password(password, user.password):
                # manually store user id in session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('home')
            else:
                return render(request, 'login.html', {'p_error': 'Incorrect Password'})
        except Login.DoesNotExist:
            return render(request, 'login.html', {'error': 'No user found ,Create an account'})
    return render(request, 'login.html')


def logout_user(request):
    # Clear session data
    request.session.flush()  # Clear all session data
    return redirect('login')