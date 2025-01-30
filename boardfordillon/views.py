from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment, Reaction


# Create your views here.
def landing(request):
    return HttpResponse("Hello Dillon!")