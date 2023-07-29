from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list_view(request):
    all_cars = models.Car.objects.all()
    context = {"all_cars":all_cars}
    return render(request, 'my_app/list.html', context=context)

def add_view(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)
        return redirect(reverse('my_app:list'))
    else:
        return render(request, 'my_app/add.html')

def delete_view(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('my_app:list'))
        except:
            print("There's no car with such a PK")
            return redirect(reverse('my_app:list'))
    else:
        return render(request, 'my_app/delete.html') 