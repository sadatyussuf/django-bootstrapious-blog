from django.urls import path
from .views import indexView , listView, searchResultView,detailView,createView,updateView,deleteView

urlpatterns = [
    path('', indexView,name='index'),
    path('blog/', listView,name='blog'),
    path('search/', searchResultView,name='search_result'),
    path('post/create/', createView,name='post-create'),
    path('post/<int:id>/', detailView,name='post-detail'),
    path('post/<int:id>/update', updateView,name='post-update'),
    path('post/<int:id>/delete', deleteView,name='post-delete'),
]