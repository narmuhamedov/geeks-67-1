from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from . import models
from django.views import generic



class SearchView(generic.ListView):
    template_name = 'blog_lst.html'
    context_object_name = 'blog_lst'
    model = models.Blog

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
    

# def seacrh_view(request):
#     query = request.GET.get('s', '')
#     if query:
#          query_lst = models.Blog.objects.filter(title__icontains=query)
#     else:
#         return HttpResponse('Блог не найден')
#     return render(request, 'blog_lst.html', {'blog_lst':query_lst})


from django.db.models import F



class BlogDetailView(generic.DetailView):
    template_name = 'blog_detail.html'
    context_object_name = 'blog_id'
    pk_url_kwarg = 'id'
    model = models.Blog

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_blog = request.session.get('viewed_blog', [])

        if obj.pk not in views_blog:
            self.model.objects.filter(pk=obj.pk).update(views=F('views')+1)
            views_blog.append(obj.pk)
            request.session['viewed_blog'] = views_blog
            obj.refresh_from_db()
        return obj







# def blog_detail_view(request, id):
#     if request.method == 'GET':
#         blog_id = get_object_or_404(models.Blog, id=id)
#         views_blog = request.session.get('viewed_blog', [])

#         if id not in views_blog:
#             blog_id.views = F("views") + 1
#             blog_id.save()
#             blog_id.refresh_from_db()

#         views_blog.append(id)
#         request.session['viewed_blog'] = views_blog

#     return render(request, 'blog_detail.html', {'blog_id': blog_id})





class BlogListView(generic.ListView):
    template_name = 'blog_lst.html'
    model = models.Blog
    paginate_by = 2
    ordering = ['-id']
    context_object_name = 'blog_lst'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_lst'] = context['page_obj']
        return context
    





# def blog_list_view(request):
#     if request.method == 'GET':
#         #query - запрос
#         blog_lst = models.Blog.objects.all().order_by('-id')
#         paginator = Paginator(blog_lst, 2)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)
        
#     return render(request, 'blog_lst.html', {'blog_lst': page_obj})






class HelloWordView(generic.View):
    def get(self, request):
        return HttpResponse('Hello World')

# def hello_world_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Hello World!')



class AboutView(generic.View):
    def get(self, request):
        return HttpResponse('Меня зовут Радомир, я Backend разработчик!')

# def about_view(request):
#     if request.method == "GET":
#         return HttpResponse('Меня зовут Радомир!')