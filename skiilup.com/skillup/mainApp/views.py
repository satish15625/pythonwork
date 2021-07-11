
from django.templatetags.static import static
from django.shortcuts import render 
from django.contrib import admin
import requests
from api.models import Employee

# home page function
def home(request):
    return render(request, 'index.html', {})


def shop(request):
    return render(request, 'shop.html', {})

def course(request):
    return render(request, 'courses.html', {})

def blog1(request):
    return render(request, 'blog_1.html', {})

def singal(request):
    return render(request, 'single.html', {})


def blog4(request):
    return render(request, 'blog_4.html', {})

def marketing(request):
    return render(request, 'marketing.html', {})

def development(request):
    return render(request, 'development.html', {})

def business(request):
    return render(request, 'business.html', {})

def maths(request):
    return render(request, 'maths.html', {})


def about(request):
    emp = Employee.objects.all()
    #print(emp)
    return render(request, 'about.html', {'d':emp})

def contact(request):
    return render(request, 'contact.html', {})

def course1(request):
    return render(request, 'course-1.html', {})

def course2(request):
    return render(request, 'course-2.html', {})

def course3(request):
    return render(request, 'course-3.html', {})

def course4(request):
    return render(request, 'course-4.html', {})

def course5(request):
    return render(request, 'course-5.html', {})

def video(request):
    return render(request, 'video.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def tems(request):
    return render(request, 'tems.html', {})
