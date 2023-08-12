from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class TYView(TemplateView):
    template_name = "classroom/ty.html"

class TeacherCreateView(CreateView):
    model = Teacher 
    fields = "__all__"
    success_url = reverse_lazy('classroom:ty')
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherListView(ListView):
    model = Teacher 
    context_object_name = "teachers_list"
    queryset = Teacher.objects.all()

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher 
    fields = "__all__"
    success_url = reverse_lazy("classroom:teachers_list")

class TeacherDeleteView(DeleteView):
    model = Teacher 
    success_url = reverse_lazy("classroom:ty")

class ContactFormmView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:ty')
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
