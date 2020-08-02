from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.

class LoginView(LoginView):
    redirect_authenticated_user = True


def logout_request(request):
    logout(request)
    return redirect("/homepage")


def quiz_ans(request):
    return redirect('/index')
