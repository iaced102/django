from django.contrib import admin
from .models import Blog_list, Category

# Register your models here.

admin.site.register(Blog_list)
admin.site.register(Category)