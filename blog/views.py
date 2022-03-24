from django.db.models import Count,Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import CommentForm,PostForm
from .models import PostModel,AuthorModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here

def get_Author(user): 
    queryset = AuthorModel.objects.filter(name = user)
    if queryset.exists():
        return queryset[0]
    return None

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
    post = get_object_or_404(PostModel,id=id)
    categories_count = get_CategoriesCount()
    latest_posts = PostModel.objects.order_by('-timestamp')
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            form.instance.name  = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse(
                'post-detail',kwargs={'id':post.pk}
                ))
    else:
        form = CommentForm()
    context = {
        'post':post,
        'latest':latest_posts,
        'categories_count': categories_count,
        'form':form
        }
    return render(request,'post.html',context)

def createView(request):
    form = PostForm(request.POST or None, request.FILES or None)
    User = get_Author(request.user)
    title = 'Create'
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            form.instance.author  = User
            form.save()
            return redirect(reverse(
                'post-detail',kwargs={'id':form.instance.id}
                ))

    context = {
        'form':form,
        'title': title
        }
    return render(request, 'post-create.html',context)

def updateView(request,id):
    post = get_object_or_404(PostModel,id=id)
    form = PostForm( request.POST or None , request.FILES or None,instance=post)
    User = get_Author(request.user)
    title = 'Update'
    print(request.method)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            form.instance.author = User
            form.save()
        # return redirect('post-update', id=id)
            return redirect(reverse(
                'post-detail',kwargs={'id':form.instance.id}
                ))
    else:
        form = PostForm(instance=post)
    # redirect('post-update', id=id)
    context = {
        'form':form,
        'title': title
        }
    return render(request, 'post-edit.html',context)

def deleteView(request,id):
    post_to_delete = get_object_or_404(PostModel,id=id)
    post_to_delete.delete()
    return redirect('blog')