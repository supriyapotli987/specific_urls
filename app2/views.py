from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse("Welcome to bangalore")
def second(request):
    return HttpResponse("Hello good morning bangalore")
