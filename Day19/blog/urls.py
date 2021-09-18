from django.urls import path
from blog.views import my_Blog


urlpatterns = [
    path('',my_Blog.as_view(),name='my_blog')
]