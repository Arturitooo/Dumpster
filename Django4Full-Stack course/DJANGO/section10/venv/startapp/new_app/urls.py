from django.urls import path
from . import views

urlpatterns = [
    #connects example view to the url
    path('', views.example_view),
    path('variable/', views.variable_view),
]