from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse(" This is supriya from jspider")

def second(request):
    return HttpResponse("This is django class")