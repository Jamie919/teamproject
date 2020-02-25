from django.shortcuts import render
from django.http import HttpResponse
def index(request):

    return HttpResponse("Wonderland says hey there partner! <a href='/wonderland/about/'>About</a>")


def about(request):
    return HttpResponse("Wonderland says hey there is About page! <a href='/wonderland/'>Index</a>")