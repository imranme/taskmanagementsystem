from django.db import models
from TaskCategory.models import Category

# Create your models here.

class  Task(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.TextField()
    IsCompleted=models.BooleanField(default=False)
    AssignDate=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Title
    
    
