import json
from django import forms
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(req):
    return render(req, "index.html", context={"username": req.user.username})


@login_required(login_url='/login')
def welcome(req):
    return render(req, "welcome.html")


def log_in(req):
    return render(req, "login.html")


def log_out(req):
    logout(req,)
    return HttpResponseRedirect("/login")


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required": "用户名必填"})
    password = forms.CharField(label="密码", error_messages={"required": "密码必填"})
    sms_code = forms.CharField(label="验证码", error_messages={"required": "验证码必填"})


@csrf_exempt
def login_handler(req):
    if req.method == "POST":
        user_form = UserForm(req.POST)
        if user_form.is_valid():
            user_obj = user_form.cleaned_data
            is_auth = authenticate(username=user_obj.get("username"), password=user_obj.get("password"))
            if is_auth and is_auth.is_active:
                login(req, is_auth)
                return HttpResponseRedirect('/')
            else:
                return render(req, "login.html", {"retcode": 1, "stderr": "用户名或密码不正确"})
        else:
            return render(req, "login.html", {"retcode": 1, "stderr": user_form.errors})
    else:
        return HttpResponseRedirect("/login")

