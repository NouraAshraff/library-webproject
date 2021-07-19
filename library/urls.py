from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name = 'login'),
    path('afterlogin', views.afterlogin, name = 'afterlogin'),
    path('adminlogin', views.adminlogin, name = 'adminlogin'),
    path('adminpage', views.adminpage, name = 'adminpage'),
    path('update', views.update, name = 'update'),
    path('logout', views.logout, name = 'logout'),
    path('addbook', views.addBook, name = 'addbook'),
    path('updatebook', views.updateBook, name = 'updatebook'),
    path('allbooks', views.allBooks, name = 'allbooks'),
    
    path('Borrow', views.Borrow, name = 'Borrow'),
]