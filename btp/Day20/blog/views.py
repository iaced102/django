from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, request
from django.views.generic import TemplateView
from .models import Category, Blog_list

# Create your views here.


class Home(TemplateView):
    template_name = 'apps/blog/home.html'
    
    def get_context_data(self,*args, **kwargs):

        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['blog_list'] = Blog_list.objects.all()
        return context

class filter(TemplateView):
    template_name = 'apps/blog/filter.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        print('getted')
        print(str(context))
        print(self.request.GET.get('filter'))
        if self.request.GET.get('filter') == 'all':
            print('get all')
            context['blog_list'] = Blog_list.objects.all()
        else:
            print("something")
            get_value = int(self.request.GET.get('filter'))
            context['blog_list'] = Blog_list.objects.filter(category_id=get_value)
            print('something getted')
        print(context)
        return context

def Create_Item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = Category.objects.all()[int(request.POST.get('category'))]
        print(category,name)
        Blog_list.objects.create(name=name,category=category)
        return render(request,'apps/blog/create_blog.html')
    else:
        return render(request,'apps/blog/create_blog.html', {'category':Category.objects.all()})

