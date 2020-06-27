from django.contrib import admin
from django.urls import path
from .views import home,contact_entry,home2,home3

urlpatterns = [
    path('', home,name="home"),
    path('2', home2,name="home2"),
    path('3', home3,name="home3"),
    path('contact',contact_entry,name="contact"),

]