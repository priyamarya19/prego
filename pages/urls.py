from django.contrib import admin
from django.urls import path
from .views import home,contact_entry

urlpatterns = [
    path('', home,name="home"),
    path('contact',contact_entry,name="contact"),

]