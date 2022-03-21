from django.urls import path
from .views import indexView , listView, searchResultView,detailView,createView

urlpatterns = [
    path('', indexView,name='index'),
    path('blog/', listView,name='blog'),
    path('search/', searchResultView,name='search_result'),
    path('post/create/', createView,name='post-create'),
    path('post/<int:id>/', detailView,name='post-detail'),
]