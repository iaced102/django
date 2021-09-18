from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog
from django.http import HttpRequest, response

# Create your views here.

class my_Blog(TemplateView):
    template_name = 'apps/blog/my_blog.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        list_all_blog = Blog.objects.all()
        context['list_all_blog']  = list_all_blog
        return context

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            context = super().get_context_data(*args, **kwargs)
            name =self.request.POST.get('name')
            Blog.objects.create(name = name)
            return response.HttpResponse('success')