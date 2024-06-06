from django.db import models
from .constants import PROJECT_CATEGORY, RATING
from django.db.models import Avg



class Project(models.Model):
    title = models.CharField(max_length=30)
    project_category = models.CharField(max_length=20, choices=PROJECT_CATEGORY)
    description = models.TextField(max_length=200)
    technologies_used = models.TextField(max_length=150)
    image = models.ImageField(upload_to='upload', blank=False)
    
    url = models.URLField()
    def __str__(self):
        return f"Title : {self.title} -- Project Category : {self.project_category}"
    
    
class ProjectReview(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 8)])
    review = models.TextField(max_length=120)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  
    def __str__(self):
        return f"Title : {self.project.title} -- Project Category : {self.project.project_category}"

    
    def avg(self):
        average_rating = ProjectReview.objects.filter(project = self.project).aggregate(Avg('rating'))['rating__avg']
        average_rating = int(average_rating)
        return average_rating