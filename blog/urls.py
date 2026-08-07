from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world_view),
    path('about/', views.about_view),
    path('', views.blog_list_view),
    path('blog_list/<int:id>/', views.blog_detail_view),
    path('search/', views.seacrh_view),
]