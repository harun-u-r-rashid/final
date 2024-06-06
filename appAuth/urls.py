from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('login/', views.user_login , name = 'login'),
    path('register/', views.user_register, name = 'register'),
    path('logout/', views.user_logout, name = 'logout'),
    path('show_profile/', views.show_user_profile, name = 'show_profile'),
    path('profile', views.user_profile_edit, name = 'edit_profile'), 
    path('contact/', views.contact, name = "contact"), 
    path('download/', views.download_resume, name = 'download'),      
]   