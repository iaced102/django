from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name= 'home'),
    path('create_item',views.Create_Item,name='create_item'),
    path('filter',views.filter.as_view(), name='filters')
]