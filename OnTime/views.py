from django.shortcuts import render
from .models import TripInput, Starting_Stop, Ending_Stop, get_Trip_Direction
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TripInputForm
from . import mbta_api

# Create your views here.
class TripListView(ListView):
    print("ran load_stops")
    model = TripInput
    context_object_name = 'trip'

class TripCreateView(CreateView):
    model = TripInput
    #fields = ('line', 'starting_stop', 'starting_time', 'ending_stop', 'ending_time')
    form_class = TripInputForm
    success_url = reverse_lazy('trip_changelist')

class TripUpdateView(UpdateView):
    model = TripInput
    #fields = ('line', 'starting_stop', 'starting_time', 'ending_stop', 'ending_time')
    form_class  = TripInputForm
    success_url = reverse_lazy('trip_changelist')

def load_starting_stops(request):
    print("ran starting stops")

    line_id = request.GET.get('line')
    starting_stops = Starting_Stop.objects.filter(line_id=line_id).order_by('name')
    print(starting_stops)
    return render(request, 'OnTime/starting_stop_dropdown_list.html', {'starting_stops':starting_stops})

def load_ending_stops(request):
    print("ran endinf stops")

    line_id = request.GET.get('line')
    ending_stops = Ending_Stop.objects.filter(line_id=line_id).order_by('name')
    print(ending_stops)
    return render(request, 'OnTime/ending_stop_dropdown_list.html', {'ending_stops':ending_stops}) 

def load_trips(request, trip_id):
    base_url = "https://api-v3.mbta.com"

    line = request.GET.get("line")
    starting_stop = request.GET.get("starting_stop")
    ending_stop = request.GET.get("ending_stop")
    starting_time = request.GET.get("starting_time")

    print("ran load trips")

    print(starting_stop)
    #direction = get_Trip_Direction()

    #trips = mbta_api.find_trips(base_url, )
    