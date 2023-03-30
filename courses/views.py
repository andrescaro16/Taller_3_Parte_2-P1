from django.shortcuts import render
from .models import Courses

def courses(request):
    coursess = Courses.objects.all()
    return render(request, 'courses.html', {'courses':coursess})