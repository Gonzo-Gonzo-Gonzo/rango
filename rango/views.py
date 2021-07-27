from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse ("Rango says her there partner!  <a href='/rango/about'>index </a>")

def about(request):
    return HttpResponse("Rango says this is the about page  <a href='/rango/index'> about </a>")