from django.urls import path
from .views import landing 

urlpatterns = [
    path('', landing, name='landing'),  # Make landing.html the homepage
]
