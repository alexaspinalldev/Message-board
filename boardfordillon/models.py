from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
reactions = [
    ('like', 'Like'),
    ('love', 'Love'),
    ('haha', 'Haha'),
    ('wow', 'Wow'),
    ('sad', 'Sad'),
    ('angry', 'Angry')
]

class Reaction(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.Choices(names=reactions)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.reaction