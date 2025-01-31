from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Comment, Reaction
# from .forms import PostForm


# Create your views here.
class MessageList(generic.ListView):
    model = Post
    template_name = "home.html"