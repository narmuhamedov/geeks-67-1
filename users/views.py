from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models, forms

#register
def register_view(request):
    if request.method == "POST":
        form_obj = forms.CustomRegisterForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/login/')
    else:
        form_obj = forms.CustomRegisterForm()
    return render(request, 'register.html', {'form': form_obj})

#login
def auth_login_view(request):
    if request.method == "POST":
        form_obj = AuthenticationForm(data=request.POST)
        if form_obj.is_valid():
            user = form_obj.get_user()
            login(request, user)
            return redirect('/profile/')
    else:
        form_obj = AuthenticationForm()
    return render(request, 'login.html', {'form': form_obj})

#logout
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')

#profile = личный кабинет
def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    user = models.CustomUser.objects.get(id=request.user.id)

    return render(request, 'profile.html', {'user': user})