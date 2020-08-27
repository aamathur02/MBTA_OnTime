from django.shortcuts import render
from .models import Trip, Starting_Stop
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TripForm

# Create your views here.
class TripListView(ListView):
    print("ran load_stops")
    model = Trip
    context_object_name = 'trip'

class TripCreateView(CreateView):
    model = Trip
    #fields = ('line', 'starting_stop', 'starting_time', 'ending_stop', 'ending_time')
    form_class = TripForm
    success_url = reverse_lazy('trip_changelist')

class TripUpdateView(UpdateView):
    model = Trip
    #fields = ('line', 'starting_stop', 'starting_time', 'ending_stop', 'ending_time')
    form_class  = TripForm
    success_url = reverse_lazy('trip_changelist')

def load_stops(request):
    print("ran yoooload_stops")

    line_id = request.GET.get('line')
    starting_stops = Starting_Stop.objects.filter(line_id=line_id).order_by('name')
    print(starting_stops)
    return render(request, 'OnTime/stop_dropdown_list.html', {'stops':starting_stops}) 