from django.shortcuts import render
from .models import TripInput, Starting_Stop, Ending_Stop
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TripInputForm

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

#class TripResultView():
    
    #0 is outbound, 1 is inbound
   #def create_trip_list(starting_stop, ending_stop, )
    