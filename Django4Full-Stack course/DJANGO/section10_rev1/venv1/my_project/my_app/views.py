from django.shortcuts import render

# Create your views here.


def example_view(request):
    return render(request, 'my_app/example.html')


def variables_view(request):
    my_var = {'first_name': 'artur', 'last_name': 'Ito', 'some_list': [
        5, 4, 3], 'some_dict': {'inside_key': 'inside_value'}, 'user_logged_in': True}
    return render(request, 'my_app/variables.html', context=my_var)


def new_variable_view(request):
    return render(request, 'my_app/new_variables.html')
