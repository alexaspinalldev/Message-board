from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment, Reaction
from .forms import PostForm


# Create your views here.
class MessageList(generic.ListView):
    model = Post
    template_name = "home.html"

@login_required
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
        request, 'home.html', {
            'form': form, 'object_list': Post.objects.all().order_by('-date_posted')})


# views for the editing and deleting post

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('home')
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'home.html', {'form': form, 'object_list': Post.objects.all().order_by(
            '-date_posted')})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('home')
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'home.html', {'form': PostForm(), 'object_list': Post.objects.all().order_by(
            '-date_posted')})
