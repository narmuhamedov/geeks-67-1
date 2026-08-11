from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.AuthLoginView.as_view()),
    path('logout/', views.AuthLogoutView.as_view()),
    path('profile/', views.profile_view),
]