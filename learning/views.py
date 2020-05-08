from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    custom_list = [{
        "id": 1,
        "name": "Custom Element 1"
    },{
        "id": 2,
        "name": "Custom Element 2"
    }, {
        "id": 3,
        "name": "Custom Element 3"
    }]


    homepage_context = {
        "page_title": "Content Title",
        "custom_list": custom_list
    }
    return render(request, "homepage.html ", homepage_context)