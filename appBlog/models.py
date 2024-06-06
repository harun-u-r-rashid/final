from django.db import models
   
class Blog(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField(max_length=150)
    author = models.CharField(max_length = 30)
    image = models.ImageField(default=False, upload_to='upload', blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"
    