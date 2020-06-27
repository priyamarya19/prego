from django.contrib import admin
from django.urls import path
from .views import home,contact_entry,home2,home3,contact_entry2

urlpatterns = [
    path('', home2,name="home2"),
    path('2', home,name="home"),
    path('3', home3,name="home3"),
    path('contact',contact_entry,name="contact"),
    path('contact2',contact_entry2,name="contact2"),

]