from django.shortcuts import render
from .models import TripInput, Starting_Stop, Ending_Stop, get_Trip_Direction
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TripInputForm
from . import mbta_api
from django.http import HttpResponse

# Create your views here.
class TripListView(ListView):
    print("ran load_stops")
    model = TripInput
    context_object_name = 'trip'

class TripCreateView(CreateView):
    model = TripInput
    #fields = ('line', 'starting_stop', 'starting_time', 'ending_stop', 'ending_time')
    form_class = TripInputForm
    success_url = reverse_lazy('trip-changelist')

class TripUpdateView(UpdateView):
    model = TripInput
    #fields = ('line', 'starting_stop', 'starting_time', 'ending_stop', 'ending_time')
    form_class  = TripInputForm
    success_url = reverse_lazy('trip-changelist')

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

def load_trips(request, pk):
    base_url = "https://api-v3.mbta.com"

    current_input = TripInput.objects.get(pk = pk)
    line = current_input.line
    starting_stop_id = current_input.starting_stop.index
    starting_stop = current_input.starting_stop.name
    ending_stop_id = current_input.ending_stop.index
    ending_stop = current_input.ending_stop.name
    begin_time = current_input.starting_time

    travel_direction = mbta_api.find_travel_direction(starting_stop_id, ending_stop_id)

    trips = mbta_api.find_trips(base_url, travel_direction, begin_time, 'CR-Franklin', starting_stop)
    times = mbta_api.find_times(base_url, trips, starting_stop, ending_stop)
    #return HttpResponse(mbta_api.create_lines_list("https://api-v3.mbta.com")
    return HttpResponse((trips))

    