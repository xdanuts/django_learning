from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from accommodation.models import Accommodation

# Create your views here.

def index(request):
    search_term = ""
    # search_term = "None"

    try:
        search_term = request.POST['search_for_city']
        accommodation_list = Accommodation.objects.filter(location__iregex=r'^{}'.format(search_term))
    except Exception as e:

        accommodation_list = Accommodation.objects.all()

    context = {
        "accommodation_list": accommodation_list,
        "search_term": search_term
    }

    return render(request, "accommodation/index.html" , context)

def details(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)

    context = {
        'accommodation': accommodation
    }

    return render(request, "accommodation/details.html", context)

def create(request):

    return render(request, "accommodation/create.html")

def submit(request):
    name = request.POST['name']
    location = request.POST['location']
    accommodation = Accommodation(name=name, location=location)
    accommodation.save()

    return HttpResponseRedirect(reverse('accommodation:list'))

def delete(request,accommodation_id):
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)
    accommodation.delete()


    return HttpResponseRedirect(reverse('accommodation:list'))

def update(request,accommodation_id):
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)
    new_name = request.POST['name']
    new_location = request.POST['location']

    accommodation.name = new_name
    accommodation.location = new_location
    accommodation.save()

    return HttpResponseRedirect(reverse('accommodation:details', args=(accommodation_id, )))