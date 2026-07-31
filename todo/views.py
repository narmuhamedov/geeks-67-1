from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

#CREATE
def create_todo_view(request):
    if request.method == 'POST':
        form_obj = forms.TodoForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/todo_list/')
    else:
        form_obj = forms.TodoForm()
    return render(request, 'create_todo.html', {'form': form_obj})

#READ
def read_todo_view(request):
    if request.method == 'GET':
        todo_list = models.TodoModel.objects.all()
    return render(request, 'read_todo.html', {'todo_list': todo_list})

#UPDATE
def update_todo_view(request, id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    if request.method == 'POST':
        form_obj = forms.TodoForm(request.POST, instance=todo_id)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/todo_list/')
    else:
        form_obj = forms.TodoForm(instance=todo_id)
    return render(request, 'update_todo.html', {'form':form_obj, 'todo_id':todo_id})


#DELETE
def delete_todo_view(request, id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    todo_id.delete()
    return redirect('/todo_list/')