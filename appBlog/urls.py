
from django.urls import path
from . import views

urlpatterns = [
   
    path('show_blog/', views.show_blog, name = "show_blog"),
    path('add_blog/', views.add_blog, name = "add_blog"),
       
]

