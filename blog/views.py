from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})



def blog_list_view(request):
    if request.method == 'GET':
        #query - запрос
        blog_lst = models.Blog.objects.all().order_by('-id')
    return render(request, 'blog_lst.html', {'blog_lst': blog_lst})






def hello_world_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World!')

def about_view(request):
    if request.method == "GET":
        return HttpResponse('Меня зовут Радомир!')