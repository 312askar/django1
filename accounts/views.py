from django.shortcuts import render

# Create your views here.

from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout

def sign_in(request):
    print(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(
                username = data['username'],
                password = data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно авторизованы')
                else:
                    return  HttpResponse('Аккаунт неактивен')
            else:
                return HttpResponse('Вы ввели неправильные данные')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponse('Вы успешно вышли')
