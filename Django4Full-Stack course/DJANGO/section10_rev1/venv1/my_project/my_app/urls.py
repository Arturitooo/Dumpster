from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = 'my_app'


urlpatterns = [
    path('', views.example_view, name='example'),
    path('variables/', views.variables_view),
    path('new_variables/', views.new_variable_view, name='new_variable'),
]
