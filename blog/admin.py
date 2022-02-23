from django.contrib import admin
from .models import AuthorModel , CategoryModel , PostModel
# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(CategoryModel)
admin.site.register(PostModel)