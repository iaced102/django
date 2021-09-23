from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Blog_list(models.Model):
    name =models.CharField(max_length=100)

    category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name

