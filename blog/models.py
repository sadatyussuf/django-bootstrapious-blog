from pydoc import describe
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class AuthorModel(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE) 
    profile = models.ImageField()

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

class BlogModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    timestamp = models.TimeField(auto_now_add=True)
    thumb = models.ImageField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    author = models.OneToOneField(AuthorModel,on_delete=models.CASCADE)