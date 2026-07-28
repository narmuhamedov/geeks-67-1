from django.shortcuts import render
from . import models

def cars_list_view(request):
    if request.method == 'GET':
        car = models.Car.objects.all()
    return render(request, 'car_list.html', {'car': car})