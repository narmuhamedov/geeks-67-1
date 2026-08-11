from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloWordView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('', views.BlogListView.as_view()),
    path('blog_list/<int:id>/', views.BlogDetailView.as_view()),
    path('search/', views.SearchView.as_view()),
]