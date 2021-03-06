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
    categories = models.ManyToManyField(CategoryModel)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    featured = models.BooleanField(default = False)
    pm_previous = models.ForeignKey('self', related_name = 'previous_post' , on_delete = models.SET_NULL, null = True,blank= True)
    pm_next = models.ForeignKey('self', related_name = 'next_post' , on_delete = models.SET_NULL, null = True,blank= True)
    


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post-update',kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post-delete',kwargs={'id': self.id})
    
    def comments(self):
        return self.comments.all()

    @property   
    def view_count(self):
        return self.viewCount.all()

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.name.username


class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(PostModel, related_name='viewCount', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username