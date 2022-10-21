from operator import index
from django import views
from django.urls import path
from . import views

app_name = 'adventure'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name="profile"),
    path('flights/<str:arv>/<str:des>/<str:pri>', views.flights, name='flights'),
    path('comment/', views.post_method, name="comment" )
]

