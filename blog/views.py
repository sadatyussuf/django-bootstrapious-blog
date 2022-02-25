from django.http import HttpResponse
from django.shortcuts import render
from .models import PostModel
# Create your views here.

def indexView(request):
    queryset = PostModel.objects.filter(featured= True)
    latest = PostModel.objects.order_by('-timestamp')[:3]
    context={
        'posts': queryset, 
        'latest': latest
        }
    return render(request,'index.html',context)

def listView(request):
    posts = PostModel.objects.order_by('-timestamp')
    context={
        'posts': posts
        }
    return render(request,'blog.html',context)


