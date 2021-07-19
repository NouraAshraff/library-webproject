import json
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Book, Student, Admin

def home(request):
  return render(request, 'home.html')

def login(request):
  
  if request.POST.get('ToSignup'):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if Student.objects.filter(username = username).exists():
      messages.info(request, 'Username is already exist')
    elif Student.objects.filter(password = password).exists():
      messages.info(request, 'Password is already taken')
    else:
      usersignup = Student(username=username, password=password)
      usersignup.save()
    return redirect('login')

  elif request.POST.get('ToLogin'): 
    username = request.POST.get('username')
    password = request.POST.get('password')
    student_list = Student.objects.all()
    found = False
    for s in student_list:
      if s.username == username and s.password == password:
        found = True
    if found == True:
      return redirect('afterlogin')
    else:
        messages.info(request,'Invalid username or password')
        return redirect('login')  

  else:
    return render(request, 'login.html')

def afterlogin(request):
  return render(request, 'afterlogin.html')

def update(request):
  if request.POST.get('updateUsername'):
    username1 = request.POST.get('username1')
    username2 = request.POST.get('username2')
    if Student.objects.filter(username = username2).exists():
        messages.info(request, 'Error : Username is already exist')
    else:
      student_list = Student.objects.all()
      for s in student_list:
        if s.username == username1:
          s.username = username2
          s.save()
      messages.info(request, 'Updated successfully....')
    return redirect('update')

  elif request.POST.get('updateAdminUsername'):
    username1 = request.POST.get('username1')
    username2 = request.POST.get('username2')
    if Admin.objects.filter(username = username2).exists():
        messages.info(request, 'Error : Username is already exist')
    else:
      admin_list = Student.objects.all()
      for a in admin_list:
        if a.username == username1:
          a.username = username2
          a.save()
      messages.info(request, 'Updated successfully....')
    return redirect('update')

  else:
    return render(request, 'update.html')

  


def logout(request):
  return render(request, 'logout.html')


def adminlogin(request):
  
  if request.POST.get('ToSignup'):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if Admin.objects.filter(username = username).exists():
      messages.info(request, 'Username is already exist')
    elif Admin.objects.filter(password = password).exists():
      messages.info(request, 'Password is already taken')
    else:
      adminsignup = Admin(username=username, password=password)
      adminsignup.save()
    return redirect('adminlogin')

  elif request.POST.get('ToLogin'): 
    username = request.POST.get('username')
    password = request.POST.get('password')
    admin_list = Admin.objects.all()
    found = False
    for a in admin_list:
      if a.username == username and a.password == password:
        found = True   
    if found == True:
      return redirect('adminpage')
    else:
        messages.info(request,'Invalid username or password')
        return redirect('adminlogin')

  else:
    return render(request, 'adminlogin.html')



######################


def adminpage(request):
  books_list=Book.objects.all()
  return render(request, 'adminpage.html', {
    "books_list" : books_list
  })


def addBook(request):
  if request.method == 'POST':
    jsonString = request.body
    bookDetails = json.loads(jsonString)
    bookname = bookDetails['bookname']
    authname = bookDetails['authname']
    isbn = bookDetails['isbn']
    isborrowed = bookDetails['isborrowed']
    borrowingperiod = bookDetails['borrowingperiod']
    publicationyear = bookDetails['publicationyear']
    book = Book.objects.create(
      BookName=bookname,
      AuthorName=authname,
      ISBN=isbn,
      isBorrowed=isborrowed,
      borrowingPeriod=borrowingperiod,
      PublicationYear=publicationyear,
    )

    return HttpResponse("Book is created successfully")
  else:
    return render(request,'addbook.html')  

def updateBook(request):
  bookId = request.GET.get('id')
  bookObj = Book.objects.get(id=bookId)
  if request.method == 'POST':
    jsonString = request.body
    bookDetails = json.loads(jsonString)
    bookname = bookDetails['bookname']
    authname = bookDetails['authname']
    isbn = bookDetails['isbn']
    isborrowed = bookDetails['isborrowed']
    borrowingperiod = bookDetails['borrowingperiod']
    publicationyear = bookDetails['publicationyear']
    Book.objects.filter(id=bookId).update(
      BookName=bookname,
      AuthorName=authname,
      ISBN=isbn,
      isBorrowed=isborrowed,
      borrowingPeriod=borrowingperiod,
      PublicationYear=publicationyear,
    )
    return HttpResponse("Updated!")
  else:
    return render(request,'updatebook.html', {
      "book": bookObj
    })

def allBooks(request) :
  return render(request,'allbooks.html')

##################
def Borrow (request):
 
  Book.isBorrowed=1
  return

