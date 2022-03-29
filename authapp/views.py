from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.forms import UserLoginForm


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