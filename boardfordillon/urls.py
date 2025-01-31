from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.MessageList.as_view(), name='home'),
    path('post_form/', views.post_form, name='post_form'),
    path('posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
