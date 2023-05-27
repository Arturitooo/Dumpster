from django.urls import path
from . import views

urlpatterns = [
    path('<str:topic>/', views.news_view),
    # it allows to create dynamic adress
    path('<int:num1>/<int:num2>', views.add_view)
]
