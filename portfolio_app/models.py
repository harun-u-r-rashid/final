from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from .constants import PROJECT_CATEGORY, RATING
from django.db.models import Avg
from auth_app.models import Account

    
    
    
class Skill(models.Model):
    title = models.CharField(max_length = 30)
    skill_category = models.CharField(max_length = 30)
    description = models.TextField()
    def __str__(self):
        return f"{self.title}"


class Blog(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    author = models.CharField(max_length = 30)
    image = models.ImageField(default=False, upload_to='upload', blank=False)
    create_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"
    
class Contact(models.Model):
    name = models.CharField(null = False, max_length = 30)
    email = models.EmailField(null = True)
    number = models.CharField(null = False, max_length = 11)
    description = models.TextField()
       
    def __str__(self):
        return f"{self.name}"
    
    
    
class Project(models.Model):
    title = models.CharField(max_length=30)
    project_category = models.CharField(max_length=20, choices=PROJECT_CATEGORY)
    description = models.TextField()
    technologies_used = models.TextField()
    image = models.ImageField(upload_to='upload', blank=False)
    
    url = models.URLField()
    def __str__(self):
        return f"Title : {self.title} -- Project Category : {self.project_category}"
    
    
class ProjectReview(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 8)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  
    def __str__(self):
        return f"Title : {self.project.title} -- Project Category : {self.project.project_category}"

    
    def avg(self):
        average_rating = ProjectReview.objects.filter(project = self.project).aggregate(Avg('rating'))['rating__avg']
        return average_rating
    
   
class Resume(models.Model):
    file = models.FileField()
    