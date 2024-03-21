
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('show_blog/', views.show_blog, name = "show_blog"),
    path('add_blog/', views.add_blog, name = "add_blog"),
    path('show_skill/', views.show_skill, name = 'show_skill'),
    path('add_skill/', views.add_skill, name = 'add_skill'),
    path('show_project/', views.show_project, name = 'show_project'),
    path('add_project/', views.add_project, name = 'add_project'),
    path('project_details/<str:title>', views.project_details, name = 'project_details'),
    path('review/', views.project_review, name='review'),
    #path('show_review/<str:title>', views.show_review, name = 'show_review'),
    path('download/', views.download_resume, name = 'download'),     
]