from django.urls import path
from . import views

urlpatterns = [
   path('', views.home),  # Home page
    path('about/', views.about),  # About page
    path('contact/', views.contact),  # Contact page
]