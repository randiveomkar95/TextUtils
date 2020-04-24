'''
(c) learning 2020

Purpose: This is the file where we can handle home page operation

'''
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request,"learning/index.html")
