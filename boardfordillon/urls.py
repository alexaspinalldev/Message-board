from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.MessageList.as_view(), name='Home'),
]