from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

#CREATE

class CreateTodoView(generic.CreateView):
    template_name = 'create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)
    




# def create_todo_view(request):
#     if request.method == 'POST':
#         form_obj = forms.TodoForm(request.POST, request.FILES)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('/todo_list/')
#     else:
#         form_obj = forms.TodoForm()
#     return render(request, 'create_todo.html', {'form': form_obj})

#READ

class ReadTodoView(generic.ListView):
    template_name = 'read_todo.html'
    model = models.TodoModel
    context_object_name = 'todo_list'

    def get_queryset(self):
        return self.model.objects.all()


class DetailTodoView(generic.DetailView):
    template_name = 'todo_detail.html'
    context_object_name = 'todo_id'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)


# def read_todo_view(request):
#     if request.method == 'GET':
#         todo_list = models.TodoModel.objects.all()
#     return render(request, 'read_todo.html', {'todo_list': todo_list})

#UPDATE

class UpdateTodoView(generic.UpdateView):
    template_name = 'update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'
    context_object_name = 'todo_id'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)
        

# def update_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     if request.method == 'POST':
#         form_obj = forms.TodoForm(request.POST, instance=todo_id)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('/todo_list/')
#     else:
#         form_obj = forms.TodoForm(instance=todo_id)
#     return render(request, 'update_todo.html', {'form':form_obj, 'todo_id':todo_id})


#DELETE
class DeleteTodoView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'todo_id'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)
        


# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     todo_id.delete()
#     return redirect('/todo_list/')