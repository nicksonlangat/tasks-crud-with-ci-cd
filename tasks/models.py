from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
