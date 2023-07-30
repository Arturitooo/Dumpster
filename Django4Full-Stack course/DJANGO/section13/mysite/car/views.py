from django.shortcuts import render, redirect
from django.urls import path, reverse
from .forms import ReviewForm

# Create your views here.

def rental_review(request):
    #POST REQUEST --> Form content -->
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            #print(form.cleaned_data) <-- would've use it if not ModelForm
            return redirect(reverse('car:ty'))
        else:
            print(form.errors)
    else:
    #ELSE, RENDER FORM
        form = ReviewForm()
        return render(request, 'car/rental_review.html', context = {"form":form})

def thank_you(request):
    return render(request, 'car/ty.html')