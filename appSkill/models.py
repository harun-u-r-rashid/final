from django.db import models
      
class Skill(models.Model):
    title = models.CharField(max_length = 30)
    skill_category = models.CharField(max_length = 100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='upload', blank=False)
    def __str__(self):
        return f"{self.title}"
