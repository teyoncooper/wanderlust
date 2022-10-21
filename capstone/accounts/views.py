from curses.ascii import HT
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout



def index(request):
    return HttpResponse('Register Account')

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout(request):
    logout(request)
    return HttpResponse(reverse("adventure:index"))




