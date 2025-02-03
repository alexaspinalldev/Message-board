from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment, Reaction
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Q


# Create your views here.
class MessageList(generic.ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reactions'] = [
            ('like', 'Like'),
            ('love', 'Love'),
            ('haha', 'Haha'),
            ('wow', 'Wow'),
            ('sad', 'Sad'),
            ('angry', 'Angry')
        ]
        return context

    def get_queryset(self):
        return Post.objects.annotate(
            like_count=Count('reaction', filter=Q(reaction__reaction='like'))
        )



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
    return render(request, 'post_form.html', {'form': form})


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


@login_required
@require_POST
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    reaction, created = Reaction.objects.get_or_create(
        post=post,
        user=request.user,
        reaction='like'
    )
    if not created:
        reaction.delete()
        liked = False
    else:
        liked = True
    like_count = Reaction.objects.filter(post=post, reaction='like').count()
    return JsonResponse({'liked': liked, 'like_count': like_count})


def home(request):
    posts = Post.objects.annotate(like_count=Count('reaction', filter=models.Q(reaction__reaction='like')))
    return render(request, 'home.html', {'posts': posts})
