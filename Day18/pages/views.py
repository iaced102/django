from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home(request):
    return HttpResponse('phuc cuc ki dep trai')