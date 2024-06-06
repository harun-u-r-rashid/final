from django.db import models
   
    
    
class Skill(models.Model):
    title = models.CharField(max_length = 30)
    skill_category = models.CharField(max_length = 30)
    description = models.TextField()
    def __str__(self):
        return f"{self.title}"
