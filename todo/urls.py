from django.urls import path
from . import views

urlpatterns = [

    path('create_todo/', views.CreateTodoView.as_view()),
    path('todo_list/', views.ReadTodoView.as_view()),
    path('todo_list/<int:id>/',views.DetailTodoView.as_view()),
    path('todo_list/<int:id>/update/', views.UpdateTodoView.as_view()),
    path('todo_list/<int:id>/delete/', views.DeleteTodoView.as_view()),
]