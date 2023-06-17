from django.contrib import admin
from car_rental.models import Car  # import the model first
# alternative .models

# Register your models here.
# admin.site.register(Car)


class CarAdmin(admin.ModelAdmin):
    # fields = ['year', 'brand']
    # changing order of class variables

    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']})
    ]
    # the part above is about adding kinda "sections" for data in django admin panel


admin.site.register(Car, CarAdmin)
