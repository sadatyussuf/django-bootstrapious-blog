from django.urls import path
from .views import indexView , listView
urlpatterns = [
    path('', indexView,name='index'),
    path('blog/', listView,name='blog'),
]