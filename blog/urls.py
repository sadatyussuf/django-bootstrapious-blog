from django.urls import path
from .views import indexView , listView, searchResultView,detailView

urlpatterns = [
    path('', indexView,name='index'),
    path('blog/', listView,name='blog'),
    path('search/', searchResultView,name='search_result'),
    path('post/<int:id>/', detailView,name='post-detail'),
]