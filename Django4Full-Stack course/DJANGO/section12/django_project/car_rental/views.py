from django.shortcuts import render
from . import models  # we need to import models to get data from DB
# Create your views here.


def list(request):
    # the all_cars variable downloads all the objects from DB
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'car_rental/list.html', context=context)


def add(request):
    return render(request, 'car_rental/add.html')


def delete(request):
    return render(request, 'car_rental/delete.html')
