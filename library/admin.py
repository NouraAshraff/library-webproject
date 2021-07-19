from django.contrib import admin
from .models import Admin, Student, Book

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Book)