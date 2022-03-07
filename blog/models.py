from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField


User = get_user_model()
class AuthorModel(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE) 
    profile_pic = models.ImageField()

    def __str__(self):
        return self.name.username
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class PostModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    content = HTMLField('Content')
    timestamp = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    categories = models.ManyToManyField(CategoryModel)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    featured = models.BooleanField(default = False)


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'id':self.id})

 

    def __str__(self):
        return self.title