from django.http import HttpResponse
from django.shortcuts import render
from .models import PostModel
# Create your views here.
def indexView(request):
    queryset = PostModel.objects.filter(featured= True)
    return render(request,'index.html',context={'posts': queryset})