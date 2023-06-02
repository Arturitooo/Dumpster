from django.urls import path
from . import views

# it register app namespace
# URL names
app_name = 'my_app'

urlpatterns = [
    # connects example view to the url
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('inheritance/', views.inheritance_view, name='inheritance'),
]
