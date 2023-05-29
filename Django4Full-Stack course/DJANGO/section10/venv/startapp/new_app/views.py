from django.shortcuts import render

# Create your views here.
def example_view(request):
    #the line below refers to the last part of startapp/new_app/templates/new_app/example.html
    return render(request, 'new_app/example.html')

def variable_view(request):

    my_var = {'first_name':'Rosaline', 'last_name':'Frank', 'some_list':[1,2,3], 'some_dict':{'inside_key':'inside_value'}}

    return render(request, 'new_app/variable.html', context = my_var)