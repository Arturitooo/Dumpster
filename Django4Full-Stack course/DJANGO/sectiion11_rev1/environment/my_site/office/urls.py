from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_of_patients, name='list_of_patients')
]
