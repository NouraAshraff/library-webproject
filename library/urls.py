from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name = 'login'),
    path('afterlogin', views.afterlogin, name = 'afterlogin'),
    path('adminlogin', views.adminlogin, name = 'adminlogin'),
    path('adminpage', views.adminpage, name = 'adminpage'),
    path('Borrow', views.Borrow, name = 'Borrow'),
    path('addbook', views.addBook, name = 'addbook'),
    path('updatebook', views.updateBook, name = 'updatebook'),
]