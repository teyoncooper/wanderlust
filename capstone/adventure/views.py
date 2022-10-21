from cgitb import text
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import Profile, Comment
from django.contrib.auth.models import User

def index(request):
    all_comments = Comment.objects.order_by('-time_created')
    context = {
        'all_comments': all_comments
    }
    if request.method == 'POST':
        post_method(request)

    return render(request, 'capstone.html', context)


def profile(request):
    print(request.user)
    flightInfo = Profile.objects.all().filter(user=request.user)
    print(flightInfo)
    user_comments = Comment.objects.order_by('-time_created').filter(user=request.user)
    context = {
        'flightInfo': flightInfo,
        'user_comments': user_comments
    }
    return render(request, 'profile.html', context)

def flights(request,arv,des,pri):
    user = User.objects.get(username=request.user.username)
    savedFlightData = Profile(user=user, price=pri, departing=des, arriving=arv)
    savedFlightData.save()
    return HttpResponseRedirect(reverse('adventure:profile'))



def post_method(request):
    comment_data = request.POST.get('comment')
    if comment_data != '':
        Comment.objects.create(text=comment_data, user=request.user)
    else:
        print("no input")

    return HttpResponseRedirect(reverse('adventure:index'))

    