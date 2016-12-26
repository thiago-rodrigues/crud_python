from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


class AuthView(View):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(AuthView, self).dispatch(*args, **kwargs)


class LoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        user = authenticate(username=request.POST['usuario'],
                            password=request.POST['senha'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/produtos/')
        else:
            return HttpResponseRedirect('/login/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')
