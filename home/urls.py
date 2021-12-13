from django import views
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('resume', views.resume, name="resume"),
    path('contact', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),    
]