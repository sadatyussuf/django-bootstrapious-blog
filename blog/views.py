from django.db.models import Count,Q
from django.shortcuts import render
from .models import PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def searchResultView(request):
    posts = PostModel.objects.all()
    q = request.GET.get('q')
    qs = posts.filter(
        Q(title__icontains= q ) |
        Q(description__icontains= q )
        ).distinct()
    context = {'queryset':qs}
    return render(request,'search_results.html',context)

def get_CategoriesCount():
    qs = PostModel.objects.values('categories__name').annotate(Count('categories'))
    return qs

def indexView(request):
    queryset = PostModel.objects.filter(featured= True)
    latest = PostModel.objects.order_by('-timestamp')[:3]
    context={
        'posts': queryset, 
        'latest': latest
        }
    return render(request,'index.html',context)

def listView(request):
    categories_count = get_CategoriesCount()
    post_list = PostModel.objects.all()
    latest_posts = PostModel.objects.order_by('-timestamp')

    paginator = Paginator(post_list,4)

    # page_var = 'page'
    page = request.GET.get('page',1)
    try:
        paginator_qs = paginator.page(page)

    except PageNotAnInteger:
        paginator_qs = paginator.page(1)

    except EmptyPage:
        paginator_qs = paginator.page(paginator.num_pages)

    context={
        # 'posts': posts
        'posts': paginator_qs,
        'latest':latest_posts,
        'categories_count': categories_count
        }
    return render(request,'blog.html',context)

def detailView(request,id):
    return render(request,'post.html')
