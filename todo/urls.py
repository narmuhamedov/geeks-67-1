from django.urls import path
from . import views

urlpatterns = [

    path('create_todo/', views.create_todo_view),
    path('todo_list/', views.read_todo_view),
    path('todo_list/<int:id>/update/', views.update_todo_view),
    path('todo_list/<int:id>/delete/', views.delete_todo_view),

]