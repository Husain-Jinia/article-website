from distutils.command.upload import upload
from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=256, default="")
    description = models.TextField(default="")
    image = models.ImageField(default = 'default.jpeg', upload_to = 'articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
