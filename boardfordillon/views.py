from django.shortcuts import render
from django.views import generic
from .models import Post, Comment, Reaction

# Create your views here.
class MessageList(generic.ListView):
    model = Post
    template_name = "home.html"

