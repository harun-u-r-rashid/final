
from django.urls import path
from . import views

urlpatterns = [
    path('show_skill/', views.show_skill, name = 'show_skill'),
    path('add_skill/', views.add_skill, name = 'add_skill'),
   
]