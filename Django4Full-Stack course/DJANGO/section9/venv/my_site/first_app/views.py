from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

articles = {
    "sports": "Sports page",
    "finance": "Finance page",
    "politics": "Politics page"
}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR")  # 404.html


def add_view(request, num1, num2):
    # domain.com / first_app / num1/ num2 --> num1 + num2
    add_result = num1 + num2
    result = f"The result of adding {num1} and {num2} is {add_result}"
    return HttpResponse(str(result))
    # allows to create dynamic adress
