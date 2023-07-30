from django import forms
from .models import Review
from django.forms import ModelForm

#class ReviewForm(forms.Form):
#    first_name = forms.CharField(label="First name", max_length=30)
#    last_name = forms.CharField(label="Last name", max_length=100)
#    email = forms.EmailField(label="Email")
#    review = forms.CharField(label="Please provide your rental feedback here:", widget= forms.Textarea(attrs={"class":"myform"}), max_length=500)

#alternative for the solution above
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        #alternatively fields = "__all__"
        fields = ['first_name','last_name', 'stars']

        #labels = {'first_name':'Custom label for it', 'last_name... etc}
