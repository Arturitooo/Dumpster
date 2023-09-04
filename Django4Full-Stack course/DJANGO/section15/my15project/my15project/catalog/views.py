from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Book, Author, Book_instance, Genre, Language
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required #this line along with line #29 allows only logged in users to go to the website
from django.contrib.auth.mixins import LoginRequiredMixin #the same as decorator above but for class based views line #23
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    num_of_books = Book.objects.all().count()
    num_of_instances = Book_instance.objects.all().count()
    num_of_instances_available = Book_instance.objects.filter(status__exact='a').count() 

    context = {
        'num_books':num_of_books,
        'num_instances':num_of_instances,
        'num_instances_available':num_of_instances_available,
    }

    return render(request, 'catalog/index.html', context = context)

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'

class BookDetail(DetailView):
    model = Book

@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'

class CheckedOutBooks(LoginRequiredMixin, ListView):
    model = Book_instance
    template_name = 'catalog/profile.html'
    paginate_by = 10

    def get_queryset(self):
        return Book_instance.objects.filter(borrower = self.request.user).all()