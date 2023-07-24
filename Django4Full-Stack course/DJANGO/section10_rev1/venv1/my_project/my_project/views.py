from django.shortcuts import render

def custm_page_not_found_view(request, exception):
    return render(request, 'error404.html', status=404)