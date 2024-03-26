# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from . import forms
from django.conf import settings


class MyPasswordChangeView(PasswordChangeView):
    form_class = forms.MyPasswordChangeForm

def logout_user(request:HttpRequest):
    logout(request)
    return redirect('login')

def signup_page(request:HttpRequest):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', {'form': form})

@login_required
def photo_profile(request:HttpRequest):
    form = forms.profilePhotoForm()
    if request.method == 'POST':
        form = forms.profilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/profile_photo.html', {'form': form})