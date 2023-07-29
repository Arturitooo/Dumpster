from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('list/', views.list_view, name='list'),
    path('add/', views.add_view, name='add'),
    path('delete/', views.delete_view, name='delete'),
]
