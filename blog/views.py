from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from . import models


def seacrh_view(request):
    query = request.GET.get('s', '')
    if query:
         query_lst = models.Blog.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден')
    return render(request, 'blog_lst.html', {'blog_lst':query_lst})


from django.db.models import F

def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
        views_blog = request.session.get('viewed_blog', [])

        if id not in views_blog:
            blog_id.views = F("views") + 1
            blog_id.save()
            blog_id.refresh_from_db()

        views_blog.append(id)
        request.session['viewed_blog'] = views_blog

    return render(request, 'blog_detail.html', {'blog_id': blog_id})



def blog_list_view(request):
    if request.method == 'GET':
        #query - запрос
        blog_lst = models.Blog.objects.all().order_by('-id')
        paginator = Paginator(blog_lst, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        
    return render(request, 'blog_lst.html', {'blog_lst': page_obj})






def hello_world_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World!')

def about_view(request):
    if request.method == "GET":
        return HttpResponse('Меня зовут Радомир!')