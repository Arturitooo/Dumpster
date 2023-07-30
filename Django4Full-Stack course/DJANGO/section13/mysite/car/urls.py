from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('rental_review/', views.rental_review, name = "rental_review"),
    path('ty/', views.thank_you, name = 'ty'),
]
