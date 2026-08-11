from django.shortcuts import render
from . import models
from django.views import generic


class CarListView(generic.ListView):
    template_name = 'car_list.html'
    context_object_name = 'car'
    model = models.Car

    def get_queryset(self):
        return self.model.objects.all()



# def cars_list_view(request):
#     if request.method == 'GET':
#         car = models.Car.objects.all()
#     return render(request, 'car_list.html', {'car': car})