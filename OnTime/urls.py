from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.TripListView.as_view(), name = 'trip_changelist'),
    path('add/', views.TripCreateView.as_view(), name = 'trip_add'),
    path('<int:pk>/', views.TripUpdateView.as_view(),name = 'trip_change'),

    path('ajax/load-starting_stops/', views.load_starting_stops, name='ajax_load_starting_stops'),  # <-- this one here
    path('ajax/load-ending_stops/', views.load_ending_stops, name='ajax_load_ending_stops'),

    path('ajax/load-trips/', views.TripResultView, name = 'ajax-load-trips'),
]