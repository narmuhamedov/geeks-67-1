from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField(blank=True) # blank=True поле не обзятельное для заполнения
    person_name = models.CharField(max_length=20, default='Иванов Иван')
    url_blog = models.URLField(blank=True)
    views = models.PositiveIntegerField(default=0, null=True)
    created_at = models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.title
