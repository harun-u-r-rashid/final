
from django.urls import path
from . import views

urlpatterns = [
   
   
    path('show_project/', views.show_project, name = 'show_project'),
    path('add_project/', views.add_project, name = 'add_project'),
    path('project_details/<str:title>', views.project_details, name = 'project_details'),
    path('review/', views.project_review, name='review'),
       
]