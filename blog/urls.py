from django.urls import path
from .views import indexView , listView, searchResultView
urlpatterns = [
    path('', indexView,name='index'),
    path('blog/', listView,name='blog'),
    path('search/', searchResultView,name='search_result'),
]