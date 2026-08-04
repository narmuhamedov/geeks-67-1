from django.db import models
from blog.models import Blog
class TodoModel(models.Model):
    title = models.CharField(max_length=20)
    TASKS = (
        ('не выполнено❌', 'не выполнено❌'),
        ('в процессе⌛', 'в процессе⌛'),
        ('выполнено✅', 'выполнено✅')
    )
    task = models.CharField(max_length=100, choices=TASKS)
    problem = models.TextField(blank=True)
    screenshots = models.FileField(upload_to='todo/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title