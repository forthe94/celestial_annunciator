from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import UserLoginForm, AuthUserCreationForm, \
    AuthUserChangeForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'title': 'FlyScanner - Вход'
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = AuthUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/auth/login/')
    else:
        form = AuthUserCreationForm()

    context = {
        'form': form,
        'title': 'FlyScanner - Регистрация'
    }
    return render(request, 'authapp/registration.html', context)


def edit(request):
    if request.method == 'POST':
        form = AuthUserChangeForm(request.POST, request.FILES,
                                  instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AuthUserChangeForm(instance=request.user)

    context = {
        'form': form,
        'page_title': 'FlyScanner - Редактирование',
    }
    return render(request, 'authapp/update.html', context)
