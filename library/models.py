from typing import Any
from django.db import models
from django.db.models.fields import CharField
from django import forms

class Student(models.Model):
    username = CharField(max_length=10, unique=True)
    password = CharField(max_length=10, unique=True)
    MyBooks =[]

    def __str__(self):
        return self.username
    
class Admin(models.Model):
    username = CharField(max_length=6, unique=True)
    password = CharField(max_length=6, unique=True)

    def __str__(self):
        return self.username


class Book (models.Model):
    BookName= models.CharField(max_length=50)
    AuthorName= models.CharField(max_length=50)
    ISBN= models.CharField(max_length=20)
    isBorrowed =models.BooleanField(default=0)
    borrowingPeriod =models.IntegerField(default=0)
    PublicationYear= models.DateField(null=True)
    def __str__ (self):
        bookinfo= self.BookName +"(" + self.ISBN +")" 
        return bookinfo 

