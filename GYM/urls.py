from django.contrib import admin
from django.urls import path
from GYM import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('pricing',views.pricing,name="pricing"),
    path('courses',views.courses,name="courses"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('logout',views.logout,name="logout"),
]