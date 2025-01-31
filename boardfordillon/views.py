from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Comment, Reaction
from .forms import PostForm


# Create your views here.
class MessageList(generic.ListView):
    model = Post
    template_name = "home.html"


# @login_required
def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(
        request, 'home.html', {'form': form, 'object_list': Post.objects.all().order_by(
            '-date_posted')})

