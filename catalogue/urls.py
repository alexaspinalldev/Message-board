from . import views
from django.urls import path

urlpatterns = [
    path('catalogue/', views.CoffeeList.as_view(), name='Catalogue'),
    path('catalogue/mylistings/', views.CoffeeMyList.as_view(), name='My listings'),
    path('catalogue/<int:product_ID>/', views.coffee_detail, name='Coffee detail'),
    path('catalogue/<int:product_ID>/delete/', views.coffee_delete, name='coffee_delete'),
    path('catalogue/<int:product_ID>/edit/', views.coffee_edit, name='coffee_edit'),
    path('catalogue/add/', views.coffee_add, name='coffee_add'),
]