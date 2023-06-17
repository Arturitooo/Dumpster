from django.shortcuts import render, redirect
from . import models  # we need to import models to get data from DB
# Create your views here.
from django.urls import reverse


def list(request):
    # the all_cars variable downloads all the objects from DB
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'car_rental/list.html', context=context)


def add(request):
    if request.POST:
        # add the car
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('car_rental:list'))
    else:
        return render(request, 'car_rental/add.html')


def delete(request):
    if request.POST:
        # delete the car
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('car_rental:list'))
        except:
            print("pk not found")
            return redirect(reverse('car_rental:list'))
    else:
        return render(request, 'car_rental/delete.html')
